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
    cnt = 0
    while i < len(textSet):
        print(i+1)
        print("Tweet Summary:")
        print(textSet[i])       
        if picSet[i] is not "":
            print("\nPicture Description:")
            print(despSet[cnt])
            cnt = cnt+1
        i =i+1
        print("----------------------------------------")

        

if __name__ == '__main__':
    try:
        inputAccount = "@AnimalPlanet"
    except:
        print("Oops! There is no twitter account!")
    else:
        entryAPI(inputAccount)

    
