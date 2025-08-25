from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import csv
import time


# ---------------------- Scraper Functions ---------------------- #

def make_driver():
    """
    Create a Safari WebDriver.
    Make sure Safari > Develop > Allow Remote Automation is enabled.
    """
    return webdriver.Safari()


def scrape_page_links(driver):
    #Scrape stories from a single Hacker News page.
    wait = WebDriverWait(driver, 10)
    links = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.titleline a"))
    )

    rows = []
    ts = datetime.now().isoformat(timespec="seconds")
    for a in links:
        title = a.text.strip()
        href = a.get_attribute("href")
        if title and href:
            rows.append({"title": title, "link": href, "scraped_at": ts})
    return rows


def scrape_hn_top(n=30):
    # Scrape top n Hacker News stories (multi-page)."""
    driver = make_driver()
    all_rows = []
    page = 1
    try:
        while len(all_rows) < n:
            driver.get(f"https://news.ycombinator.com/news?p={page}")
            page_rows = scrape_page_links(driver)
            all_rows.extend(page_rows)
            page += 1
        return all_rows[:n]
    finally:
        driver.quit()


def save_csv(rows, path="hackernews_top.csv"):
    # Save scraped stories to CSV.
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["index", "title", "link", "scraped_at"])
        w.writeheader()
        for i, r in enumerate(rows, start=1):
            w.writerow({"index": i, **r})
    print(f"Successfully Saved {len(rows)} stories to '{path}'.")


def open_links_in_browser(rows, delay=0.6):
    # Open all scraped links in the default browser with optional delay.
    for r in rows:
        webbrowser.open_new_tab(r["link"])
        time.sleep(delay)


def filter_by_keyword(rows, keyword):
    #return only rows where the title contains the keyword.
    return [r for r in rows if keyword.lower() in r["title"].lower()]


# ---------------------- CLI ---------------------- #

def main():
    print("\nHacker News Top Stories Scraper\n")

    # Ask user to tell quantity of stories to scrape otherwise defualt 10 set
    try:
        n = int(input("Number of top stories to scrape? (e.g., 10, 30, 50) [default 10]: ") or 10)
    except ValueError:
        n = 10

    auto_open = input("Open links in browser after scraping? (y/N): ").strip().lower() == "y"
    keyword = input("Filter stories by keyword (optional, leave blank for all): ").strip()

    print(f"\nScraping top {n} stories from Hacker News...\n")
    rows = scrape_hn_top(n=n)

    # keyword filter if given
    if keyword:
        rows = filter_by_keyword(rows, keyword)
        print(f"\nFiltered stories by keyword '{keyword}': {len(rows)} found.\n")

    # Print results
    for i, r in enumerate(rows, 1):
        print(f"{i}: {r['title']} -> {r['link']}")

    # Save CSV with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"hackernews_top{n}_{timestamp}.csv"
    save_csv(rows, filename)

    # Optionally open links
    if auto_open:
        print("\nOpening links in browser...")
        open_links_in_browser(rows)

    print("\nDone!")


if __name__ == "__main__":
    main()


