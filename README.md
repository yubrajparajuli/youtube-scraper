# YouTube Comment Scraper

A Python tool to scrape comments from YouTube videos for research purposes.

## Purpose

This project collects YouTube comments for **hate speech detection research**.
The data is used purely for academic and research purposes.

## Data

Comments are collected using the official YouTube Data API v3.
All data is stored in the `data/` folder.

## Setup

1. Clone the repo
2. Install dependencies:

```
pip install google-api-python-client pandas

```

3. Add your YouTube Data API key in `scraper.py`
4. Run:

```
python scraper.py

```

## Disclaimer

All data collected is publicly available on YouTube.
This tool is intended for research purposes only.
