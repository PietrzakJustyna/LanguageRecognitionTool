import preparation_functions
import numpy as np
from config import max_letters, language_tags
import pandas as pd

word_data = []
language_data = []
master_dic = []

count = 0

for tag in language_tags.keys():
    print('generating dictionary for ' + tag)
    dic = preparation_functions.generate_dictionary(tag, max_letters)
    for word in dic:
        master_dic.append(word)
    vct = preparation_functions.convert_dic_to_vector(dic, max_letters)
    for vector in vct:
        word_data.append(vector)
    output_vct = preparation_functions.create_output_vector(count, len(language_tags))
    for i in range(len(vct)):
        language_data.append(output_vct)
    count += 1

arr = []
for i in range(len(word_data)):
    entry = []
    entry.append(master_dic[i])
    for digit in language_data[i]:
        entry.append(float(digit))
    for digit in word_data[i]:
        entry.append(float(digit))
    arr.append(entry)


arr = np.array(arr)
np.save('arr.npy', arr)
df = pd.DataFrame(arr)
df.to_csv('data.csv')
