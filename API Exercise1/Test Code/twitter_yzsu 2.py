import re
import tweepy
import wget
import urllib 
import os
import requests
import io



# Imports the Google Cloud client library
# from google.cloud import vision

# from google.cloud.vision import types
from os import listdir


#Twitter API credentials
consumer_key = "0gzrWgU42coZopvSul5XWIyIl"
consumer_secret = "CI2Q8x1suBlPsfz3y5QkRqI62rpgdYZQKM552d6Y69x8L0b4Y1"
access_key = "920759443759026177-4NdyCaI36qzRMOk2pbuiRZ2dLHpDWoP"
access_secret = "7PqhynxGdD0Ci4Qxb1okbm96C1srMCimTeDiI20vL5gkr"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))

    media_files = set()
    for status in alltweets :
        try:
            media = status.extended_entities.get('media', [])
        except:
            media = status.entities.get('media', [])
        if(len(media) > 0):
            for i in range(len(media)):
             media_files.add(media[i]['media_url'])

    for media_file in media_files:

        print(media_file)
        wget.download(media_file)
  
   
#     # client = vision.ImageAnnotatorClient()


#     m=1

#     OBJ = [pic for pic in listdir() if pic.endswith('jpg')]
#     for i in OBJ:
#         file_name = os.path.join(os.path.dirname(__file__),i)
  
    

# # Loads the image into memory
#         with io.open(file_name, 'rb') as document_file:
#              content = document_file.read()
#         file = open("label.txt","w")
#         image = types.Image(content=content)

#         # Performs label detection on the image file
#         response = client.label_detection(image=image)
#         labels = response.label_annotations
        
#         print('Labels:')
#         file.write('Lables:')
#         for label in labels:
#            file.write(label.description+'\n')
#            print(label.description)
        
#         file.close()
    os.system("ffmpeg -framerate 5 -pattern_type glob -i '*.jpg'     -c:v libx264 -r 30 -pix_fmt yuv420p video.mp4")

            
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@YZHSU")

