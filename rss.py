import requests
import feedparser

webhook_url = 'https://discord.com/api/webhooks/webhookid'
    # You need to create a discord webhook on the specific channel that you want the script to use and then past that URL above.
rss_url = 'https://feed.example.com/feed/all/'
    # URL of the RSS feed, should support all standard RSS feed types

def send_to_discord(message):
    payload = {'content': message}
    requests.post(webhook_url, json=payload)

def get_last_entry():
    try:
        with open('last_posted.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def update_last_entry(link):
    with open('last_posted.txt', 'w') as file:
        file.write(link)

def check_rss_feed():
    feed = feedparser.parse(rss_url)
    latest_entry = feed.entries[0]
    last_posted_entry = get_last_entry()

    if latest_entry.link != last_posted_entry:
        send_to_discord(f"New post 📰: {latest_entry.title} - {latest_entry.link}")
        update_last_entry(latest_entry.link)

check_rss_feed()
