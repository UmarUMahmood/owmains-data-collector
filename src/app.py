import os, auth

reddit = auth.request()
os.system("clear")


def get_subreddits(reddit):
    # use my multireddit to get the overwatch mains subreddits
    subreddits = reddit.multireddit("umarrii", "owmains").subreddits
    return subreddits


def get_subcounts(subreddits):

    subcounts = []
    sub = {}

    for subreddit in subreddits:
        sub = {
            "sub_name": subreddit.display_name.capitalize(),
            "sub_count": subreddit.subscribers,
        }
        subcounts.append(sub)

    # sort the list by name (subreddits starting in lowercase were at the end)
    subcounts = sorted(subcounts, key=lambda k: k["sub_name"])

    return subcounts


subreddits = get_subreddits(reddit)
subcounts = get_subcounts(subreddits)

for subcount in subcounts:
    print(subcount)
