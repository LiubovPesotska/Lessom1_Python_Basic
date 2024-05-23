import string
def generate_hashtag(s: str) -> str:
    s = ''.join(char for char in s if char not in string.punctuation)
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    hashtag = '#' + ''.join(capitalized_words)
    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag

print(generate_hashtag('Python Community'))
print(generate_hashtag('i like python community!'))
print(generate_hashtag('Should, I. subscribe? Yes!'))