import redis
from eve import Eve

# start an instance of Redis
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

# start the Eve app using Redis
app = Eve(redis=r)

# run the Eve app broadcasting it publically
app.run(host='0.0.0.0')
