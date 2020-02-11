import re
import wikipediaapi as wiki
from unidecode import unidecode
import config


def generate_dictionary(tag, max_word_length):
    wiki.Wikipedia(tag)
    for topic in config.language_tags[tag]:
        page = wiki.Wikipedia(language=tag, extract_format=wiki.ExtractFormat.WIKI).page(topic)
        content = page.text
        content = unidecode(content)
        final = process(content, max_word_length)
    return final


def process(page_content, max_word_length):
    words = re.sub(r'[^a-zA-Z ]', '', page_content)
    lower = words.lower()
    word_list = lower.split()
    short_words = [word for word in word_list if len(word) <= max_word_length]
    return short_words

