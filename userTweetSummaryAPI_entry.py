import getUserTwAPI
import googlePicDescribeAPI


def entryAPI(youTwitterAccount):
    print("----------------------------------------")
    print("Twittwer Account: " + youTwitterAccount)
    print("----------------------------------------")
    #fetch top 20 tweet 
    allSet = getUserTwAPI.get_all_tweets(youTwitterAccount)
    #describe picture
    despSet = googlePicDescribeAPI.googlePicDescribeAPI("picsTweet")
    i= 0
    textSet = allSet[0]
    picSet = allSet[1]
    if len(textSet) == 0:
        return("No Account!")
    cnt = 0
    while i < len(textSet):
        print(i+1)
        print("Tweet Summary:")
        print(textSet[i])       
        if picSet[i] !=  "":
            print("\nPicture Description:")
            print(despSet[cnt])
            cnt = cnt+1
        i =i+1
        print("----------------------------------------")
    return("Success!")

 

        
        
      

if __name__ == '__main__':
    entryAPI("@AnimalPlanet")

    
