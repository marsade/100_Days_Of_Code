# Day 45 - Beautiful Soup

## Concepts
- Beautiful Soup parses a page's HTML so you can pull out specific elements
- `select()` takes CSS selectors (`".titleline a"`); `find_all()` takes a tag name and attributes (`name="h3", class_="title"`)
- `getText()` returns an element's text; `.get("href")` returns an attribute
- Add `/robots.txt` to a site's base URL to see what it allows you to scrape
- `Crawl-delay` is how many seconds to wait between requests; if none is listed, scrape no more than once a minute
- Captchas exist to block bots, and scraping has legal and ethical limits, so check the site's terms first

## Project: Best movies scraper
**Goal:** Scrape Empire's best movies list and save the titles in order to `movies.txt`.
**How it works:** `requests` fetches an archived (Wayback Machine) copy of the page. Beautiful Soup finds every `h3` with class `title`, and the titles go into a list. The page counts down from the bottom, so the list is reversed before being written one title per line.
**Run it:** `pip install requests beautifulsoup4`, then `python main.py`
**What I'd improve:** number the titles ("1) Title").

## Code worth reusing
```python
# Get all scores as ints, then find which post has the most
article_upvote = [int(s.getText().split()[0]) for s in soup.find_all("span", class_="score")]
top_vote = article_upvote.index(max(article_upvote))
```

## What confused me
- None so far

## Real-world use
Collecting public data (prices, listings, headlines) automatically, after checking robots.txt.