# more simplistic than gathering text from an API
# in this version one provides the text to test the sentiment analysis

# Importing TextBlob package

from textblob import TextBlob

print("\nHere is the most basic of Sentiment Analysis.\n")
text1 = 'Python is boring'
text2 = 'Python is the most superior programming language!'

# attempting to pass the texts to a dataframe to be able to print sentiments of multiple text blocks
obj = TextBlob(text1)
sentiment = obj.sentiment.polarity
print(text1, ", Sentiment: ", sentiment)

obj = TextBlob(text2)
sentiment = obj.sentiment.polarity
print(text2, ", Sentiment: ", sentiment)
# simple, inputted text demonstration
