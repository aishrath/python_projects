# Aishwareeya Rath
# Copyright 2020

from __future__ import print_function

try:
    import praw
    import os
    import redis
except ImportError as ie:
    print("ErrorImportingModules", ie)
except ImportError as configError:
    print("UnableToImportConfig", configError)


DEBUG = True
MAX_ERROR_COUNT = 10000
SHORT_SLEEP = 1
LONG_SLEEP = 10000
TOTAL_COUNT = 0
usr = "USER"
pwd = "PASSWORD"
sec = "SECRET"
clid = "CLIENT_ID"
desc = "DESCRIPTION"


def connect_to_reddit():
    try:
       CONN = praw.Reddit(
            user_agent=desc,
            client_id=clid,
            client_secret=sec,
            username=usr,
            password=pwd,
        )
    except Exception as ConnectionError:
        print(ConnectionError)
        return False
    return True


def get_comments():
    try:
        pub = redis.Redis(
            host="HOST",
            port=0000,
            db=0,
            password="PASSWORD"
            socket_timeout=None,
            connection_pool=None,
            charset="utf-8",
            errors="strict",
            unix_socket_path=None,
        )

        for comment in CONN.subreddit("all").stream.comments():
            comment = str(comment.body.encode("utf-8"))
            print("Publishing message to channel - " + comment)
            pub.publish("REDIS_DB_CHANNEL", comment)
    except Exception as ex:
        print("CouldNotPostMessage", ex)


if __name__ == "__main__":
    try:
        if connect_to_reddit():
            while True:
                if ERROR_COUNT <= MAX_ERROR_COUNT:
                    try:
                        get_comments()
                    except Exception as e:
                        ERROR_COUNT += 1
                        print("EncounteredError", e)
                else:
                    ERROR_COUNT = 0
    except KeyboardInterrupt:
        print("Thanks! See you next time!")
