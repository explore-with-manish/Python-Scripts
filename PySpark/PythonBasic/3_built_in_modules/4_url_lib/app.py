# from urllib.request import urlopen

# with urlopen("http://sixty-north.com/c/t.txt") as story:
#     story_words = []
#     for line in story:
#         line_words = line.decode("utf-8").split()
#         for word in line_words:
#             story_words.append(word)

# print(story_words)

# -------------------------------------

# import urllib.request

# x = urllib.request.urlopen("https://www.google.com")
# # print(x.read())

# fo = open("my-google.html", "w+")
# fo.write(str(x.read()))

# -------------------------------------

import urllib.request

headers = {}

headers["user-agent"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
)

req = urllib.request.Request("https://www.google.com/search?q=bajaj", headers=headers)
# print(x.read())

res = urllib.request.urlopen(req)
resData = res.read()

fo = open("google-response.html", "w+")
fo.write(str(resData))
