import json
from pprint import pprint as pp

# fo = open("data.json", "r")
fo = open("posts.json", "r")
data = json.load(fo)

pp(data)
