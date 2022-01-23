import os, auth, datetime
from db.db import connection, query, fetch, update, load_subreddits

reddit = auth.request()
conn = connection()

os.system("clear")


def get_subreddits(reddit):
    # use my multireddit to get the overwatch mains subreddits
    subreddits = reddit.multireddit("umarrii", "owmains").subreddits
    return subreddits


def find_new_subreddits(subreddits):

    # get the subreddits from db
    db_subreddits = load_subreddits(conn)

    # only need the subreddit names
    db_subs = []
    for db_subreddit in db_subreddits:
        db_subs.append(db_subreddit["subreddit_name"])

    # get subreddit names from the multireddit
    subs = []
    for subreddit in subreddits:
        sub = subreddit.display_name.capitalize()
        subs.append(sub)

    # compare both subreddit names
    s = set(db_subs)
    new_subreddits = [x for x in subs if x not in s]

    return new_subreddits


def save_subreddits_to_db(new_subreddits):
    sql_add_subreddit = "INSERT INTO subreddit (subreddit_name) VALUES (%s)"

    for new_subreddit in new_subreddits:
        update(conn, sql_add_subreddit, new_subreddit)
        print(f"Added {new_subreddit} to db.")


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
    sql_add_subcount = (
        "INSERT INTO subcount (day, subreddit_id, subscribers) VALUES (%s, %s, %s)"
    )

    db_subreddits = load_subreddits(conn)

    day = datetime.date.today()

    for subcount in subcounts:
        for db_subreddit in db_subreddits:

            if db_subreddit["subreddit_name"] == subcount["sub_name"]:
                subreddit_id = db_subreddit["subreddit_id"]

        update(conn, sql_add_subcount, (day, subreddit_id, subcount["sub_count"]))


print("Getting subreddits from multireddit.")
subreddits = get_subreddits(reddit)

print("Checking for new subreddits.")
new_subreddits = find_new_subreddits(subreddits)

if new_subreddits != []:
    print("Found new subreddits.")
    save_subreddits_to_db(new_subreddits)
    print("Finished adding new subreddits to db.")
else:
    print("No new subreddits found.")

print("Getting subcounts.")
subcounts = get_subcounts(subreddits)

print("Saving subcounts.")
save_subcounts(subcounts)
print("Saved subcounts.")
