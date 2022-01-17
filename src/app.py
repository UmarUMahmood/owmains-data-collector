import os, auth, datetime
from db.db import connection, query, fetch, update, load_subreddits

reddit = auth.request()
conn = connection()

os.system("clear")


def get_subreddits(reddit):
    # use my multireddit to get the overwatch mains subreddits
    subreddits = reddit.multireddit("umarrii", "owmains").subreddits
    return subreddits


def get_subcounts(subreddits):

    subcounts = []
    sub = {}

    # get the name and subscriber count of each subreddit
    for subreddit in subreddits:
        sub = {
            "sub_name": subreddit.display_name.capitalize(),
            "sub_count": subreddit.subscribers,
        }
        subcounts.append(sub)

    # sort the list by name (subreddits starting in lowercase were at the end)
    subcounts = sorted(subcounts, key=lambda k: k["sub_name"])

    return subcounts


def save_subcounts(subcounts):
    sql_add_subcount = "INSERT INTO subcount (day, subreddit_id, subscribers) VALUES (%s, %s, %s)"
    
    db_subreddits = load_subreddits(conn)
    
    day = datetime.date.today()
    
    for subcount in subcounts:
        for db_subreddit in db_subreddits:

            if db_subreddit["subreddit_name"] == subcount["sub_name"]:
                subreddit_id = db_subreddit["subreddit_id"]

        update(conn, sql_add_subcount, (day, subreddit_id, subcount["sub_count"]))

    print("Saved subcounts.")


subreddits = get_subreddits(reddit)
subcounts = get_subcounts(subreddits)
save_subcounts(subcounts)
