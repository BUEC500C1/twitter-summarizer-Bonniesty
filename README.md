# Twitter Summary API Doc

# description
This is an API that will return one user's recent 20 twitter feed summary (Twitter Feeds and picture text description )
 - Input: Twitter account Name
 - Output: Console will display the feed summary (feeds and picture description). Pictures are downloaded in ```picsTweet``` folder.
 
# how to use
You can access the API by running the entry file ```userTweetSummaryAPI_entry.py``` 
- First, install the package listed in ```requirements.txt```, including Tweepy and Google Vision API.
- Second, get twitter API credentials and Google Vision API credentials json file. Input twitter credentials in ```getUserTwAPI.py``` and google credentials in the json file. For security reason, I delete these credentials. If you need them, please contact me. 
- Third, import userTweetSummaryAPI_entry.entryAPI, and input the Account name in the bracket. If you basically run this file, the account is default set to @AnimalPlanet.
```python
python userTweetSummaryAPI_entry.py
```

# API design workflow
This userTweetSummaryAPI contains two sub APIs:  ```getUserTweetAPI``` and ```googlePicDescribeAPI```.
- You can use the first API to fetch text and pictures from selected twitter acount, and the pictures will be downloaded in the folder.
- The second API will load the pictures from firt API and use google vision API to generate described labes of the picture. 
- Also, you can run the two sub APIs seperately.


```python
python getUserTweetAPI.py
```
```python
python googlePicDescribeAPI.py
```

# CB and CI
This API has passed pytest testcase and github checks.
![image](https://github.com/BUEC500C1/twitter-summarizer-Bonniesty/blob/master/examplePic/CBCI.png)

However, for security reason, I have to delete all the credentials and the checks will temporarely fail.  

# Example
I use the account @AnimalPlanet and summary the 20 tweet feeds & related pictures.

