import tweepy

print('This is my bot')

CONSUMER_KEY = 'LZ9TmatXA3mu3cR4OAMjEXnVA'
CONSUMER_SECRET = 'Dv0uvp7q6rbCr4INJPJSldoq1VOJQHazJHWWzE5s7m0j5mAf0H'
ACCESS_KEY = '1212817544995688448-IXxR53oy5lKqO7ox1GLsVLIsTj93KQ'
ACCESS_SECRET = '1J6qOltFKXz0fL0nk9G5cT9rywihFWpBy8bz4WeADXx5r'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status('Testing from the fridge')