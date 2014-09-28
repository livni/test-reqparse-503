import random
import string
import json
import requests


def rand_string(size):
    return ''.join([random.choice(string.letters) for x in xrange(size)])

for i in xrange(1, 5):
    print 'Test', i
    for j in xrange(5):
        r = requests.post('http://test-request-size.herokuapp.com/test' + str(i),
                          data=json.dumps({'something': rand_string(50000)}),
                          headers={'content-type': 'application/json', 'accept': 'text/plain'})
        print r.status_code
