tweet_limit = 280
tweet_string = 'Blah' * 50
if daff := tweet_limit - len(tweet_string) >= 0:
    print('A fitting tweet')
else:
    print('Went over by', abs(daff))
