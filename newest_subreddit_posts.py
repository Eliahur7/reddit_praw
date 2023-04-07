# this will be working within a specific sub and will return the 20 newest post

import praw
import pandas as pd

reddit = praw.Reddit(
    client_secret = <client_secret>,
    client_id = <client_id>,
    password = <password>,
    user_agent = <user_agent>,
    username = <username>
)

# list for df conversion
_posts = []
# this will return 20 (could be modified) new posts from you subreddit of choice


new_bets = reddit.subreddit("subreddit name").new(limit=20)
# return the important attributes
for post in new_bets:
    _posts.append(
        [
            post.id,
            post.author,
            post.title,
            post.score,
            post.num_comments,
            post.selftext,
            post.created,
            post.pinned,
            post.total_awards_received,
        ]
    )

# create a dataframe
_posts = pd.DataFrame(
    _posts,
    columns=[
        "id",
        "author",
        "title",
        "score",
        "comments",
        "post",
        "created",
        "pinned",
        "total awards",
    ],
)
# this (_posts) will get datetime details of each post
_posts["created"] = pd.to_datetime(_posts["created"], unit="s")
_posts["created date"] = pd.to_datetime(_posts["created"], unit="s").dt.date
_posts["created time"] = pd.to_datetime(_posts["created"], unit="s").dt.time

print(_posts)
