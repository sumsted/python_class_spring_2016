from bottle import route, run, template, static_file, get, post, request
from tweet import post_tweet, get_tweets

# http://bottlepy.org/docs/dev/tutorial.html

@get('/')
def get_index():
    tweets = get_tweets()
    return template('index',tweets=tweets)


@post('/tweet')
def tweet():
    tweet_status = request.forms.get('tweet-status')
    post_tweet(tweet_status)
    tweets = get_tweets()
    return template('index', tweets=tweets)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


run(host='0.0.0.0', port=8080)#, reloader=True)
