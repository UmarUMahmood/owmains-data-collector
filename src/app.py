import os
import auth

reddit = auth.request()

os.system("clear")

print(reddit.user.me())
