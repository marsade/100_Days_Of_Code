# Day 46 - Musical Time Machine
 
Pick a date, and this script builds a playlist of the Billboard Hot 100 songs from that day, on both **YouTube Music** and **Spotify**.
 
Built for Day 46 of the 100 Days of Code Python course, on Linux with Vim.
 
## How it works
 
1. Asks for a date in `YYYY-MM-DD` format and keeps asking until it gets a valid one.
2. Scrapes the Hot 100 chart for that date with `requests` and Beautiful Soup, from the [BakeBoard Hot 100 archive](https://appbrewery.github.io/bakeboard-hot-100/).
3. Checks your existing playlists and picks a new name (e.g. `1999-05-01 Time Machine`) that doesn't clash with one you already have.
4. **YouTube Music:** creates the playlist, searches each song, and adds the top match.
5. **Spotify:** searches each song (limited to a year either side of your date), collects the track URIs, creates a private playlist, and adds them all in one call.
Songs that can't be found are reported in the terminal and skipped, so one bad match doesn't stop the rest.
 
## Tech stack
 
- Python 3
- [Requests](https://pypi.org/project/requests/) and [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/) for scraping
- [Spotipy](https://spotipy.readthedocs.io/) for the Spotify Web API (OAuth)
- [ytmusicapi](https://ytmusicapi.readthedocs.io/) for YouTube Music
- [python-dotenv](https://pypi.org/project/python-dotenv/) for secrets



