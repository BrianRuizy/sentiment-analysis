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
      
    userInput = input("Enter text for AI: ");
    while userInput != 'q':

      sentiment = TextBlob(userInput).sentiment.polarity
      print ('Sentiment: ', sentiment)  # Concatenation
      print('Positive\n' if sentiment > 0 else 'Negative\n' )  # Ternary operator

      sentiment_analysis() # recursion
    
sentiment_analysis() # call function
