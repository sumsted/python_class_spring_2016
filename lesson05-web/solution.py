from bottle import route, run, template, static_file, get, post, request
from tweet import post_tweet, get_tweets

# http://bottlepy.org/docs/dev/tutorial.html

@get('/')
def get_index():
    # call get_tweets from the tweet module, sotre the result in a variable called tweets 
    tweets = get_tweets()
    # return the result of the function template, pass two parameters to template()
    # the first parameter is the name of our html file in a string, simple.html, but leave
    # off the .html
    # the second is a named parameter, call it tweets and assign tweets to it
    return template('simple',tweets=tweets)


@post('/tweet')
def tweet():
    # notice that we're pulling the value of tweet-status from the request
    # this is what you typed into the web form
    tweet_status = request.forms.get('tweet-status')
    
    # call post_tweet from module tweet, pass in the tweet_status
    post_tweet(tweet_status)

    # call get_tweets from the tweet module, sotre the result in a variable called tweets 
    tweets = get_tweets()
    
    # just as you did in the get_index() function call template and return its result
    return template('simple', tweets=tweets)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


run(host='0.0.0.0', port=8080)#, reloader=True)
