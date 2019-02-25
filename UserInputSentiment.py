#more simplistic than gathering text from an API
#in this version one provides the text to test the sentiment analysis

#Importing TextBlob package
#repl.it allows for seamless package installation!

from textblob import TextBlob

text1 = 'Python is lame'
text2 = 'Python is the most superior programming language!'

#attempting to pass the texts to a dataframe to be able to print sentiments of multiple text blocks
obj = TextBlob(text1)
sentiment = obj.sentiment.polarity
print(text1, ": ", sentiment)

obj = TextBlob(text2)
sentiment = obj.sentiment.polarity
print(text2, ": ", sentiment )
#simple, inputted text demonstration
