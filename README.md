# Reddit Data Scraper (PRAW API)

A robust Python utility designed to scrape and process data from Reddit using the **PRAW (Python Reddit API Wrapper)**. This tool is built for developers and researchers looking to perform sentiment analysis, monitor subreddits, or gather datasets for machine learning.

## 🚀 Key Features
* **Subreddit Monitoring:** Extract the newest posts from any specific subreddit.
* **Trend Analysis:** Identify popular posts and trending topics across Reddit.
* **Data Export:** Structured data collection ready for analysis in Pandas or SQL.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Library:** [PRAW](https://praw.readthedocs.io/)
* **Focus:** Data Engineering, Web Scraping, API Integration

## 📋 Configuration
To use this scraper, you must have a Reddit Developer account. Obtain your credentials at [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).

```python
import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="YOUR_USER_AGENT",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD"
)
