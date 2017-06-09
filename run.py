from eve import Eve
from eve.auth import BasicAuth
import redis


class SimpleAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # find administrators from the DB
        administrators = app.data.driver.db['administrators']
        # try to find an admin account matching the given auth
        this_admin = administrators.find_one({'username': username,
                                              'password': password})

        # if the credentials match an admin account, return true
        if this_admin:
            return True
        # otherwise return false and block access
        else:
            return False


if __name__ == '__main__':
    # start an instance of Redis
    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

    # instantiate Eve api
    app = Eve(auth=SimpleAuth, redis=r)

    # start the API broadcasting globally
    app.run(host='0.0.0.0')
