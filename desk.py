import redis
from datetime import timedelta
import json
class DBManager(object):
    def __init__(self):
        self.r = redis.Redis()
    def add_activity(self,key,value):
        self.r.set(key,value)
    def get_activity(self,key):
        return self.r.get(key)
    def get_id(self):
        keys = redis.keys('*')
        i = 0
        for key in keys:
            i += 1
        return i
class ActivityEntity:
    def __init__(self,activity_type,user_id,timestamp):
        self.activity_type = activity_type
        self.user_id = user_id
        self.timestamp = timestamp
    def todict(self):
         d = {}
         d["type"]    =    self.activity_type
         d["user_id"]   =    self.user_id
         d["timestamp"] =    self.timestamp
         return d
    def tojsonstring(self):
        return json.dumps(self.todict())
class redisservice:
    def __init__(self,db):
        self.db = db
        last_id = self.db.get_id
        self.idfactory = idfactory(last_id)
    def add_activity(self, activity):
        key = str(new_id)
        new_id = self.idfactory.get_new_id()
        value = activity.tojsonstring()
        self.db.add_activity(key, value)
class idFactory:
    def __init__(self,last_id):
        self.last_id = last_id
    def get_new_id(self):
        self.last_id += 1
        new_id = self.last_id + 1
        return new_id
#db = DBManager()
#db.add_activity("Hello","7")
#print(db.get_activity("Hello"))
a = ActivityEntity("break", 910, 1290456)
d = a.tojsonstring()
print(d)