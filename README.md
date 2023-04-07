# reddit_praw
praw api to scrape data off of reddit for analysis
for every API call using PRAW, the below snippet of code should be added
reddit = praw.Reddit(
   
    client_secret = <client_secret>,
    client_id = <client_id>,
    password = <password>,
    user_agent = <user_agent>,
    username = <username>
)
enter the relevant values for the client params below, make sure to encrypt/hide and not expose in public
