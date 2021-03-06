#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tweepy 
import urllib


#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(account_name):

    #authorization
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #get 20 tweets of user
    alltweets = []
    new_tweets = api.user_timeline(screen_name = account_name,count=20)
    alltweets.extend(new_tweets)

    #save user tweets and picture
    picSet = []
    textSet= []
    for status in alltweets:
        #text
        textSet.append(status.text)
        #picture
        mediaData = status.entities.get('media',[])
        if(len(mediaData) == 0):
            picSet.append('')
        else:    
            	picSet.append(mediaData[0]['media_url'])

    #print(textSet)
    #print(picSet)


    #download image    
    index = 0 
    cnt = 0
    for pic in picSet:
        if pic != '':
            cnt = cnt+1
            urllib.request.urlretrieve(pic,"./picsTweet/pic%03d.jpg"%index)
        index = index +1    
    if cnt == 0:
        print("No picture in this account!")

    print("Finished Loading!!")  
    allSet = []
    allSet.append(textSet)
    allSet.append(picSet)
    return allSet

def getUserTwAPI(account_name):
    try:
        get_all_tweets(account_name)
        return("success!")
    except Exception:
        print("The account is invalid!!")
        
                         

if __name__ == '__main__':   
    getUserTwAPI("@AnimalPlanet")

