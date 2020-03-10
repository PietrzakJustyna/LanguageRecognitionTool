import tensorflow.keras.models as models
from tensorflow.keras.layers import Dense, Dropout
from tool.preparation_functions import convert_dic_to_vector
from tool.config import max_letters, language_tags
from unidecode import unidecode
import numpy as np

network = models.Sequential()
network.add(Dense(200, input_dim=26*max_letters, activation='sigmoid'))
network.add(Dense(150, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dropout(0.15))
network.add(Dense(75, activation='sigmoid'))
network.add(Dense(len(language_tags), activation='softmax'))

network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
network.load_weights('tool/weights.h5')


# while True:
#     dic = []
#     valid = False
#     while not valid:
#         print('Let our predictor decide if the word is in Polish or English')
#         word = input('Enter word to predict (maximum 10 characters, do not use special characters):\n')
#         if len(word) <= max_letters:
#             word = word.lower()
#             valid = True
#         else:
#             print('Word must be less than ' + str(max_letters + 1) + ' letters long')
#
#     dic.append(word.lower().strip())
#     vct_str = convert_dic_to_vector(dic, max_letters)
#     vct = np.zeros((1, 26 * max_letters))
#     count = 0
#     for digit in vct_str[0]:
#         vct[0, count] = int(digit)
#         count += 1
#     prediction_vct = network.predict(vct)
#
#     langs = list(language_tags.keys())
#     for i in range(len(language_tags)):
#         lang = langs[i]
#         score = prediction_vct[0][i]
#         print(lang + ': ' + str(round(100*score, 2)) + '%')
#     print('\n')


def predict(word):
    dic = []
    word = unidecode(word.lower().replace(" ", ""))
    dic.append(word.lower().replace(" ", ""))
    vct_str = convert_dic_to_vector(dic, max_letters)
    vct = np.zeros((1, 26 * max_letters))
    count = 0
    for digit in vct_str[0]:
        vct[0, count] = int(digit)
        count += 1
    prediction_vct = network.predict(vct)

    langs = list(language_tags.keys())
    result = ""
    for i in range(len(language_tags)):
        lang = langs[i]
        score = prediction_vct[0][i]
        result += lang + ': ' + str(round(100*score, 2)) + '%' + '\n'
    return result
