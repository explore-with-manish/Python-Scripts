# from urllib.request import urlopen

# with urlopen('http://sixty-north.com/c/t.txt') as story:
#     story_words = []
#     for line in story:
#         line_words = line.decode('utf-8').split()
#         for word in line_words:
#             story_words.append(word)

# print(story_words)

# -------------------------------------------------------------

# import urllib.request

# x = urllib.request.urlopen("https://www.bajajfinserv.in/")
# # print(x.read())

# fo = open("bajaj.html", "w+")
# fo.write(str(x.read()))

import urllib.request

# Fetch the webpage content
x = urllib.request.urlopen("https://www.bajajfinserv.in/")
content = x.read()

# Decode bytes to a string and remove all newline characters
content_str = content.decode("utf-8").replace("\n", "")

# Save the cleaned content to an HTML file
with open("bajaj.html", "w", encoding="utf-8") as fo:
    fo.write(content_str)

# ------------------------------------------------------------

# import urllib.request

# # headers = {}

# # headers['user-agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
# req = urllib.request.Request("https://www.google.com/search?q=Synechron")

# res = urllib.request.urlopen(req)
# resData = res.read()

# fo = open("googleResponse.html", "w+")
# fo.write(str(resData))

# --------------------------------------- JSON

# import urllib.request
# from pprint import pprint as pp
# import json

# URL = "https://jsonplaceholder.typicode.com/posts"

# # Creating the Request object without any custom headers
# req = urllib.request.Request(URL)

# # Attempting to open the URL
# res = urllib.request.urlopen(req)
# data = json.loads(res.read())
# pp(data)
