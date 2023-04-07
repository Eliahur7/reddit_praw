import praw
import json

reddit = praw.Reddit(
    client_secret = <client_secret>,
    client_id = <client_id>,
    password = <password>,
    user_agent = <user_agent>,
    username = <username>
)


#list top posts of the day
subreddit = reddit.subreddit("all") 
top_posts = subreddit.top("day", limit=10) # limit the number of posts to 10

post_list = [] # create a list
for post in top_posts:
    post_dict = {
            "subreddit": str(post.subreddit),
            "title": post.title,
            "score": post.score,
            "number of comments": str(post.num_comments),
            "url": post.url
        }
    post_list.append(post_dict)
    json_data = json.dumps(post_list, indent = 5)
    print(json_data)
