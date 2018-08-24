import tweepy
from textblob import TextBlob

#My Twitter API information
consumer_key = 'o2dmknBXaTyAClG8MWt4O45Mi'
consumer_secret = '1vrHI3RCErfEDj5g9iymxozTL5GwPUfCJE9ZZ64z6k826DGgGJ'
access_token = '1033015126000132096-prt4l70av47t3fHqsUc65WvL9R8AlT'
access_token_secret = 'QTZSKssYnjJ8Er9WmpgVn9KRLdeSRWbIQsrTfgazeGBrP'

#login using tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

public_tweets = api.search('machine learning')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
