lookup = {}
lookup = {}
lookup = {"age": 42, "loc": "Italy"}
lookup = dict(age=42, loc="Italy")

print(lookup)
print(lookup["loc"])

# lookup['cat'] # keyerror


class Wizard(object):
    def __init__(self, name, level):
        self.name = name
        self.level = level


gandolf = Wizard("Glandof", 42)
print(gandolf.__dict__)


# Suppose these came from a data source, e.g. database, web service, etc
# And we want to randomly access them

import collections

User = collections.namedtuple("User", "id, name, email")

users = [
    User(1, "user1", "user1@talkpython.fm"),
    User(2, "user2", "user2@talkpython.fm"),
    User(3, "user3", "user3@talkpython.fm"),
    User(4, "user4", "user4@talkpython.fm"),
]


for u in users:
    print(u)

print()
print()

for u in users:
    print(u.id)

print()
print()

lookup = dict()

for u in users:
    lookup[u.id] = u

print(lookup)

