#import TextBlob for analysis
#import tweepy for Twitter api access
from textblob import TextBlob
import tweepy

#token & keys accessible from 'apps.twitter.com'
consumer_key = '2EvcPmEmTwRWQoro99hcnAA5p'
consumer_secret = '8UfS6SMTNy3vljNZD5QOkr60FxYtojFPefeOndeI8URxVKKoFL'

access_token = '1045540698613788672-06C40NTIRlQRclGVArRv3vawrkH1MW'
access_token_secret = 'UP0mlyeMbA6TlBJgyND6U0xbBnDMQGHxGOdPg5JzrvBp6'

#account authentican 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#method we will use to provide TextBlob with data
api = tweepy.API(auth)
public_tweets = api.search('Trump') 

#loop to print tweets along with sentiment
for tweet in public_tweets:
  print(tweet.text)
  analysis = TextBlob(tweet.text)
  print(analysis.sentiment)
  if analysis.sentiment[0]>.075:
    print ('|Positive|', '\n')
  elif analysis.sentiment[0]<-.075:
    print ('|Negative|', '\n')
  else:
    print ('|Neutral|', '\n')

