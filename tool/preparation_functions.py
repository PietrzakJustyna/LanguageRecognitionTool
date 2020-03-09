import re
import wikipediaapi as wiki
from unidecode import unidecode
import tool.config as config


def generate_dictionary(tag, max_word_length):
    final = []
    for topic in config.language_tags[tag]:
        page = wiki.Wikipedia(language=tag, extract_format=wiki.ExtractFormat.HTML).page(topic)
        content = page.text
        content = unidecode(content)
        li = process(content, max_word_length)
        final.extend(li)
    return final


def process(page_content, max_word_length):
    words = re.sub(r'[^a-zA-Z ]', '', page_content)
    lower = words.lower()
    word_list = lower.split()
    short_words = []
    for word in word_list:
        if len(word) <= max_word_length:
            short_words.append(word)
    return short_words


def convert_dic_to_vector(dic, max_word_length):
    new_list = []
    for word in dic:
        vec = ''
        n = len(word)
        for i in range(n):
            current_letter = word[i]
            ind = ord(current_letter)-97
            placeholder = (str(0)*ind) + str(1) + str(0)*(25-ind)
            vec = vec + placeholder
        if n < max_word_length:
            excess = max_word_length-n
            vec = vec + str(0)*26*excess
        new_list.append(vec)
    print(len(new_list))
    return new_list


def create_output_vector(tag_index, number_of_languages):
    out = str(0)*tag_index + str(1) + str(0)*(number_of_languages-1-tag_index)
    return out
