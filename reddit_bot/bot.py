import praw
import re
import time

reddit = praw.Reddit(client_id="_06WxeBYkgbPnQ",
                     client_secret="	F3OKJOj62UYQotI6yJF38yVFxJw",
                     user_agent="console:reddit_bot:0.0.1 (by /u/my_reddit_bot)>",
                     username="romanoreggie",
                     password="blahblah6")

# print(reddit.read_only)

subreddits = ['programmerhumor', 'funny', 'mildlyinteresting']
pos = 0

title = "Lost programmer Joke"
url = "https://imgur.com/Zce5lQr"

def post():
    global subreddits
    global pos

    try:
        subreddit = reddit.subreddit(subreddits[pos])
        subreddit.submit(title, url=url)

        pos = pos + 1

        if (pos <= len(subreddits) - 1):
            post()
        else:
            print ("Done")
    except praw.exceptions.APIException as e:
        print e.message

post()
