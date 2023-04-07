import praw


reddit = praw.Reddit(
   
    client_secret = <client_secret>,
    client_id = <client_id>,
    password = <password>,
    user_agent = <user_agent>,
    username = <username>
)

subreddits = reddit.subreddits.popular(limit=20)  # limit the number of subreddits to 20


for subreddit in subreddits:

  print(f"{subreddit.display_name}: {subreddit.subscribers} members")
