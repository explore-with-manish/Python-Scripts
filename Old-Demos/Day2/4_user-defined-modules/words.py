# from urllib.request import urlopen

# with urlopen('http://sixty-north.com/c/t.txt') as story:
#     story_words = []
#     for line in story:
#         line_words = line.decode('utf-8').split()
#         for word in line_words:
#             story_words.append(word)

# print(story_words)

# -------------------------------------------------------------

from urllib.request import urlopen


def fetch_words():
    print("\nFrom words.py\n")
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    return (story_words)


# print(__name__)

if __name__ == "__main__":
    print(fetch_words())