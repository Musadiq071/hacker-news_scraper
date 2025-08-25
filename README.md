# Hacker News Scraper (CLI)

A lightweight Python CLI tool that scrapes top stories from [Hacker News](https://news.ycombinator.com) using Selenium (Safari WebDriver).  
Stories are saved to CSV with timestamps, and you can filter by keywords or automatically open them in your browser.

---

## Features

- Scrape any number of top Hacker News stories (e.g., 10, 30, 50)  
- Filter stories by keyword  
- Save results to CSV with timestamped filenames  
- Optionally open all links in your default browser  

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/YOUR-USERNAME/hacker-news_scraper.git
cd hacker-news_scraper
```
2. install dependencies:

pip install -r requirements.txt

3. Usage
Run the scraper

python3 automation.py

You will be prompted to enter:
Number of top stories to scrape (default 10)
Whether to open links in your browser
Optional keyword filter

-Example output in terminal:
1: Google's Liquid Cooling -> https://chipsandcheese.com/p/googles-liquid-cooling-at-hot-chips
2: chipsandcheese.com -> https://news.ycombinator.com/from?site=chipsandcheese.com

-Example csv file:
hackernews_top10_20250825_090015.csv

Notes
Requires Safari with "Allow Remote Automation" enabled:
Safari > Develop > Allow Remote Automation
Run once in terminal:

safaridriver --enable


Example Output
Check the hackernews_top10(example_file).csv in the repo for a sample of scraped stories.



   
