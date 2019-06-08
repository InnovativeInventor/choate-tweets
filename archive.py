import datetime
import json
import time

import GetOldTweets3 as got
import tweepy


class ArchiveTweet:
    def __init__(self, consumer_token, consumer_secret, access_token,
                 access_token_secret):
        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)
        if not self.api.verify_credentials():
            raise ValueError("API Creds Invalid")

        self.debug = False
        self.tweets = []

    def archive_account(self, query: str):
        ids = []
        hashtags = []
        for each_status in tweepy.Cursor(
                self.api.user_timeline, screen_name=query, count=1000).items():
            ids.append(each_status.id_str + '\n')
            for each_hashtag in each_status.entities.get('hashtags'):
                if each_hashtag['text'] not in hashtags:  # Can't wait for 3.8
                    hashtags.append(each_hashtag['text'] + '\n')
                if self.debug:
                    print(
                        each_status.user.screen_name,
                        each_status.text.strip('\n'),
                        end='\n\n')
        return ids, hashtags

    def archive_hashtag(self, query: str, full_backup=True):
        ids = []
        if full_backup:
            for each_tweet in got.manager.TweetManager.getTweets(
                    got.manager.TweetCriteria().setQuerySearch(query)):
                ids.append(str(each_tweet.id) + '\n')

        for each_status in tweepy.Cursor(
                self.api.search, q=query, count=100).items():
            ids.append(each_status.id_str + '\n')
        return ids

    def write_data(self, filename, data):
        with open(filename, 'a') as outfile:
            outfile.writelines(data)
