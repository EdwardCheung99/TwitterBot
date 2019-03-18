import tweepy
import time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

nouns_file = 'nouns.txt'

def get_nouns(nouns_file):
    nouns_f = open(nouns_file, 'r')
    nouns_list = nouns_f.readlines()
    nouns_list = [x.strip() for x in nouns_list]
    nouns_f.close()
    return nouns_list

while True:
    nouns_list = get_nouns(nouns_file)
    for noun in nouns_list:
        print('Sending out tweet')
        api.update_status('#The' + noun)
        time.sleep(14400)
    print('Nouns list completed')
    break
