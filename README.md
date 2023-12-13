# rss-discord
Python script using Discord webhooks and Feedparser to post updates fetched via RSS feeds to a specific channel.

Depends on: feedparser which can be installed using pip for Python

Just edit line #4 with the webhook URL of the channel you want it to post to and line #6 with the URL of the RSS feed

The script runs only once and writes a file last_posted.txt to the directory it's stored in.

In order to have it running "all the time" I suggest using something like a scheduled task in Windows or crontab in Linux setup like this:

*/5 * * * * python3 /home/user/rss.py

which will run the script every 5 minutes
