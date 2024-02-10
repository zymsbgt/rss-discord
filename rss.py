import os
import requests
import feedparser
import schedule
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get webhook URL and RSS feed URLs from environment variables
webhook_url = os.getenv('WEBHOOK_URL')
rss_urls = os.getenv('RSS_URLS').split(',')

def send_to_discord(message):
    payload = {'content': message}
    requests.post(webhook_url, json=payload)

def get_last_entry(index):
    try:
        with open(f'last_posted_{index}.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def update_last_entry(index, link):
    with open(f'last_posted_{index}.txt', 'w') as file:
        file.write(link)

def check_rss_feed():
    for index, rss_url in enumerate(rss_urls):
        print(index, rss_url)
        feed = feedparser.parse(rss_url)
        latest_entry = feed.entries[0]
        last_posted_entry = get_last_entry(index)

        if latest_entry.link != last_posted_entry:
            # Extracting title from the summary attribute
            title = latest_entry.summary.split('<p>')[1].split('</p>')[0]
            send_to_discord(f"New post 📰: {title} - {latest_entry.link}")
            update_last_entry(index, latest_entry.link)

check_rss_feed()
schedule.every(15).minutes.do(check_rss_feed)

while True:
    schedule.run_pending()
    time.sleep(1)
