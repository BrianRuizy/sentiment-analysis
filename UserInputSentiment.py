# This version is a more simplistic implementation
# As opposed to gathering text from an API or web scraping.
# In this version one provides the text in run-time to process for sentiment analysis

# Importing TextBlob package
from textblob import TextBlob

print("------------------------------",
      "\n| Sentiment Analysis Machine |",
      "\n|        'q' to quit         |",
      "\n------------------------------\n")


def sentiment_analysis():
    # Ask user for input
    userInput = input("Enter text to analyze: \n")

    if userInput != "q":

        obj = TextBlob(userInput)  # set object of user input
        sentiment = obj.sentiment.polarity  # pass object to text-blob library
        print("sentiment: ", sentiment, "\n")  # prints polarity

        sentiment_analysis()  # loops function again


sentiment_analysis()
print("--------------------------------",
   "\n| Thank's for using my machine |",
    "\n--------------------------------\n")


# The outputted polarity ranges from negative (-1)
# to positive (1), more neutral comments tend to give out
# a polarity between -0.2 <-> 0.2
