import os, auth

reddit = auth.request()
os.system("clear")


def get_subreddits(reddit):
    # use my multireddit to get the overwatch mains subreddits
    subreddits = reddit.multireddit("umarrii", "owmains").subreddits
    return subreddits


subreddits = get_subreddits(reddit)
print(subreddits)
