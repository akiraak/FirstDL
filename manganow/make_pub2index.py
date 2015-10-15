# -*- coding: utf-8 -*-
import json


books = []
with open("images_info.json", "r") as f:
  json_str = f.read()
  books =  json.loads(json_str)

publishers = []
for book in books:
  if not book['publisher'] in publishers:
    publishers.append(book['publisher'])

with open("publishers.json", "w") as f:
  f.write(json.dumps(publishers))
