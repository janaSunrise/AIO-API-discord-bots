IMGUR_LINKS = (
    "https://imgur.com/",
    "https://i.imgur.com/",
    "http://i.imgur.com/",
    "http://imgur.com",
    "https://m.imgur.com"
)
ACCEPTED_EXTENSIONS = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif"
)


def filter_reddit_url(url) -> str:
    if not url.startswith("https://v.redd.it/") or url.startswith("https://youtube.com/"):
        if url.startswith(IMGUR_LINKS):
            if url.endswith(".mp4"):
                url = url[:-3] + "gif"
            elif url.endswith(".gifv"):
                url = url[:-1]
            elif url.endswith(ACCEPTED_EXTENSIONS):
                url = url
            else:
                url = url + ".png"
        elif url.startswith("https://gfycat.com/"):
            url_cut = url.replace("https://gfycat.com/", "")

            url = f"https://thumbs.gfycat.com/{url_cut}-size_restricted.gif"
        elif url.endswith(ACCEPTED_EXTENSIONS):
            url = url

    return url
