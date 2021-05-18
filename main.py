#Thi sis the main part of the code. It receibe a string and give tow metrics about sentiment 
#analysis, the magnitude and score, using google cloud api natural language.

#The two metrics are score and magnitude. The score, has range -1 to 1, indicates how negative
#or positive is the declaration(-1 is the negative sentiment and 1 is positive sentiment. The magnitude, range 0 to infinite, indicates  the weight 
# of sentiment to this declaration.

# Imports the Google Cloud client library
from google.cloud import language_v1
from google.oauth2 import service_account

# Set the credentials for the project, in a json file
credentials = service_account.Credentials.from_service_account_file("chat-moderation-service-b46d1ae0187e.json")


# Instantiates a client
client = language_v1.LanguageServiceClient(credentials=credentials)

# The text to analyze
text = u"I am crazy about harry potter. I am a big fan"
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
#The two metrics are score and magnitude. The score, has range -1 to 1, indicates how negative
#or positive is the declaration(-1 is the negative sentiment and 1 is positive sentiment. The magnitude, range 0 to infinite, indicates  the weight 
# of sentiment to this declaration.