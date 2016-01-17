import tweepy

username = "classtest001"
consumer_key='WGgMJ45kp75aE1AFwKmtdz02X'
consumer_secret='4JLDBL6LWtHAuaEAEWcvGQdv0rA38XyWdESt7mt54mOCRwAKb4'
access_token='3718506375-NjC2n870SayUqGC7dK3Pp7CvLH1o5zTBOkjtCSf'
access_token_secret='YiDmYxNcmu55cn044BifipbGVfocsf9boUmWLELxhHtWD'

def get_tweets():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    num_tweets = 100
    full_tweets = api.user_timeline(screen_name=username, count=num_tweets)
    return [tweet.text.encode('utf-8') for tweet in full_tweets]

def post_tweet(tweet_status):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        status = api.update_status(status=tweet_status)
    except Exception as e:
        return -1
    return status.id

if __name__=='__main__':
    print(post_tweet('tweet test 5'))
    tweets = get_tweets()
    for tweet in tweets:
        print(tweet)
    