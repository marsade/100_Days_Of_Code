#!/usr/bin/env python3
'''Musical Time Machine with Spotify/YT and Beautiful Soup'''
import datetime as dt
import os
import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic


load_dotenv()
yt = YTMusic("browser.json")
scope = "playlist-modify-public playlist-modify-private  \
        playlist-read-private user-library-read private  \
        user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                     client_id=os.getenv("SPOTIFY_CL_ID"),
                     client_secret=os.getenv("SPOTIFY_SECRET_KEY"),
                     redirect_uri="http://127.0.0.1:9090",
                     scope=scope))
db_base_url = "https://appbrewery.github.io/bakeboard-hot-100/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:160.0) \
    Gecko/20100101 Firefox/160.0"
}

while True:
    try:
        usr_date = input("Which year do you want to travel to? \
                         Type it in this format YYYY-MM-DD:\n")
        travel_date = dt.date.fromisoformat(usr_date)
        travel_date_str = travel_date.strftime("%Y-%m-%d")
        break
    except ValueError:
        print("Invalid input. Please put in a correct date")


def avoid_duplicates(text) -> str:
    '''Return new plalist name if duplicate

    Returns:
        res(str): new playlists name'''
    dup_num = 1
    text = text.split(")")
    last_num = text[0][-1:]
    if last_num.isdigit():
        str_split = text[0][:-1]
        dup_count = int(last_num) + dup_num
        text = str_split + f"{str(dup_count)})"
        res = "".join(text)
    else:
        text += f"({str(dup_num)})"
        res = "".join(text)

    return res


def prep_pl(new_pl, user_pl):
    '''Returns new playlist name

    Returns:
        str - output of avoid_duplicates functions'''
    dup_status = False
    for pl in user_pl:
        if new_pl == pl:
            dup_status = True
            prep_pl = avoid_duplicates(new_pl)
    if dup_status:
        return prep_pl
    else:
        return new_pl


def yt_add_pl(songs) -> None:
    '''Creates Time Machine Playlist, and searches and adds \
       songs to Youtube Music'''
    existing_pl = [pl["title"] for pl in yt.get_library_playlists()]
    pl_name = f"{travel_date_str} Time Machine"
    new_pl_name = prep_pl(pl_name, existing_pl)
    playlist = yt.create_playlist(
                new_pl_name, f"Billboard Top 100 songs on {travel_date_str}"
                )

    for song in songs:
        try:
            song_res = yt.search(song, filter="songs")
            if not song_res:
                print(f"No results for: {song}")
                continue

            video_id = song_res[0]["videoId"]
            response = yt.add_playlist_items(playlist, [video_id])
            print(song, "->", response)
        except Exception as e:
            print(f"Failed on {song!r}: {type(e).__name__}: {e}")


def sp_add_pl(songs):
    '''Creates Time Machine Playlist, and searches and adds songs to Spotify'''
    existing_pl = sp.current_user_playlists()
    items = existing_pl["items"]
    user_sp_pl = []
    for item in items:
        user_sp_pl.append(item["name"])
    pl_name = f"{travel_date_str} Time Machine"
    new_pl_name = prep_pl(pl_name, user_sp_pl)

    user_id = sp.current_user()["id"]
    year = travel_date_str[0:4]
    track_uris = []
    for song in songs:
        try:
            q = f"track'{song}' year:{int(year) - 1} - {int(year) + 1}"
            track = sp.search(q=q, type="track", limit=1)
            track_uris.append(track["tracks"]["items"][0]["uri"])
        except Exception as e:
            print(f"Failed on {song!r}: {type(e).__name__}: {e}")

    playlist = sp.user_playlist_create(user_id, new_pl_name,
                                       description=f"Billboard Top 100 \
                                       songs on {travel_date_str}",
                                       public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)


db_full_url = f"{db_base_url}{travel_date_str}/"
response = requests.get(db_full_url, headers=headers)
bb_webpage = response.text
bb_soup = BeautifulSoup(bb_webpage, "html.parser")
song_names = [son.getText() for son in bb_soup.find_all(
              name="h3", class_="chart-entry__title")]

yt_add_pl(song_names)
sp_add_pl(song_names)
