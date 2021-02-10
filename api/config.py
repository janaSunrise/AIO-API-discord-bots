import os

# -- Constants definition --
USER_AGENT = "AIO-API for discord bots"

# -- Reddit variable config --
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")

# -- Subreddit config --
subreddits_list = {
    "memes": [
        "memes",
        "dankmemes",
        "funny",
        "ComedyCemetery",
        "wholesomememes",
        "meirl",
        "me_irl",
        "DeepFriedMemes",
    ]
}
