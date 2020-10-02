import string
from collections import Counter
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

stop_words = set(stopwords.words('english'))

# input text
text = """Emotional intelligence is defined as “one’s ability to know, feel and judge emotions in cooperation with a person’s thinking process for behaving in a proper way, with ultimate realisation of happiness in him and in others”.
Like general intelligence, emotional intelligence is also developed in a person by birth. Normal development of emotion leads to healthy life, but too much variation in emotional level damages the individual’s life.
The level of emotion in a person is called Emotional Quotient (EQ). This can be obtained by using emotional intelligence tests, same way as we assess the IQ of a person.
The success of a person in his job or profession depends not only on his IQ, but also on his EQ. The nurse with high emotional quotient can identify and perceive her emotions and of others like patients easily through face reading, bodily language, voice tone, etc.

Read more on Brainly.in - https://brainly.in/question/1114801#readmore."""
# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
tokenized_words = cleaned_text.split()

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
emotion_list = []


with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word  in final_words:
            emotion_list.append(emotion)
w = Counter(emotion_list)
# Plotting the emotions on the graph

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('emotion.png')
plt.show()