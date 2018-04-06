import re
import tweepy
import wget
import urllib 
import os
import requests
import io
from google.cloud import vision
from google.cloud.vision import types
from pymongo import MongoClient
import pprint
import bson
from google.cloud import vision
from google.cloud.vision import types
from os import listdir


#Twitter API credentials
consumer_key = "XXX"
consumer_secret = "XXX"
access_key = "XXX"
access_secret = "XXX"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    data ={}
    data['info'] = []
    data['info'].append({
        'name': screen_name
        })
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
        if(len(alltweets) > 10):
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
  
    os.system("ffmpeg -framerate 10 -pattern_type glob -i '*.jpg'     -c:v libx264 -r 30 -pix_fmt yuv420p production.mp4")
   
    # client = vision.ImageAnnotatorClient()

    client = vision.ImageAnnotatorClient()
    OBJ = [pic for pic in listdir() if pic.endswith('jpg')]
    for i in OBJ:
        file_name = os.path.join(os.path.dirname(__file__),i)
        counter = 1
        data['info'].append({
            'picture ' + str(counter): i 
            })

# Loads the image into memory
        with io.open(file_name, 'rb') as document_file:
             content = document_file.read()
        file = open("label.txt","w")
        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations
        
        label_list =[]
        print('Labels:')
        file.write('Lables:')
        for label in labels:
           label_list.append(label.description)
           file.write(label.description+'\n')
           print(label.description)
        data['info'].append({
            'description ' + str(counter): label_list
            })
        counter += 1
    file.close()
    client = MongoClient()
    db = client.yzsu.database
    collection = db.yzsu_collection
    posts = db.posts
    posts.insert_one(data)
    #return label.description

            
if __name__ == '__main__':
    get_all_tweets("@YZHSU")




    