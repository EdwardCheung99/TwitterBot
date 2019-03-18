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
used_nouns_f = 'usednouns.txt'

def get_nouns(nouns_file):
    nouns_f = open(nouns_file, 'r')
    nouns_list = nouns_f.readlines()
    nouns_list = [x.strip() for x in nouns_list]
    nouns_f.close()
    return nouns_list

def update_used(used_nouns_f, curr_noun):
    used_f = open(used_nouns_f, 'a')
    used_f.write(curr_noun + '\n')

def get_used_map(used_nouns_f):
    used_f = open(used_nouns_f, 'r')
    used_map = {}
    for line in used_f:
        used_map[line.strip()] = True
    return used_map

while True:
    nouns_list = get_nouns(nouns_file)
    used_map = get_used_map(used_nouns_f)
    for noun in nouns_list:
        noun = noun.lower()
        if (noun not in used_map.keys()):
            print('Sending out tweet for ' + noun)
            api.update_status('#The' + noun)
            update_used(used_nouns_f, noun)
            used_map = get_used_map(used_nouns_f)
            time.sleep(14400)
    print('Nouns list completed')
    break
