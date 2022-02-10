import tweepy

consumer_key = '3dVXAPBZA6orrETZ5povrv2vs'
consumer_secret = 'kkrzRvP5v1ar5N3n1OLA8dw64gYVhPFArzMEllA9ut8kSZCYGY'
access_token = '1172225949942910976-A6z2lzqH6Zktv6rn7Oa3OOnGQpq80m'
access_token_secret = '7sQ3oYlq8bRcuD1wf3BbAdCJqqMu1cGlrAzHq2O8gEpqo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)