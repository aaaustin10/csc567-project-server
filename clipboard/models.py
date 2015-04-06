from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import json

# Create your models here.
class Entry(models.Model):
    timestamp = models.DateTimeField(default=now)
    contents = models.CharField(max_length=1000)
    owner = models.ForeignKey(User)

    @staticmethod
    def iterable_to_json(entries):
        entry_dicts = []
        map(lambda entry: entry_dicts.append(entry.to_dict()), entries)
        return json.dumps(entry_dicts)

    @staticmethod
    def json_to_entry(json_string):
        request = json.loads(json_string)
        e = Entry()
        e.contents = request['contents']
        e.owner_id = request['owner_id']
        return e

    def to_dict(self):
        d = {}
        d['timestamp'] = str(self.timestamp)
        d['contents'] = self.contents
        d['owner_id'] = self.owner.id
        return d

    def to_json(self):
        return json.dumps(self.to_dict())
