import nltk


stop_words = set(nltk.corpus.stopwords.words('english'))

def remove_stop_words(sentence):
    filtered_sentence = []
    for word in sentence.split():
        if word not in stop_words:
            filtered_sentence.append(word)

    return ' '.join(filtered_sentence)

sentence = " Zero is an for with has no stop words."

filtered_sentence = remove_stop_words(sentence)

print(filtered_sentence)
word_counts = {}

for word in sentence.split():
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

print(word_counts)