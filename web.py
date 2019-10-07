from urllib.request import urlopen
import requests
import main
import webbrowser
import wikipedia
from pyowm import OWM
import googletrans
from googletrans import Translator
from bs4 import BeautifulSoup as soup
import os
import vlc
import youtube_dl
import urllib
import pytube
import html5lib
import urllib3
import json


def launchWeb(site):
    main.ail("launching sir...")
    Asite = '{}'.format(site.replace(" ", "").replace('launch', ''))
    if "com" in site:
        webbrowser.open('https://www.{}'.format(Asite))
    elif "org" in site:
        webbrowser.open('https://www.{}'.format(Asite))


def wiki(query):
    Aquery = '{}'.format(query.replace('tell me about', ''))
    main.ail(wikipedia.summary(Aquery, sentences=2))


def news():
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
    open_bbc_page = requests.get(main_url).json()
    article = open_bbc_page["articles"]
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        main.ail(results[i])


def weather(city_query):
    main.ail("fetching weather details sir")
    city_query_word = city_query.split()
    city_query_last = city_query.rsplit(' ', 1)[0]
    city = '{}'.format(city_query_word[-1].replace(city_query_last, ''))
    owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
    obs = owm.weather_at_place(city)
    w = obs.get_weather()
    k = w.get_status()
    x = w.get_temperature(unit='celsius')
    main.ail(
        'Current weather in %s is %s. '
        'The maximum temperature is %0.2f '
        'and the minimum temperature is %0.2f degree celcius'
        % (city, k, x['temp_max'], x['temp_min']))

def translator(string,dest):
    language = {
        'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'ne': 'nepali',
        'no': 'norwegian',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
        'fil': 'filipino',
        'he': 'hebrew'
    }

    languagecode = dict(map(reversed, language.items()))
    translator = Translator()
    translated = translator.translate(string, dest=languagecode[dest])
    main.ail('here is your translated text')
    print(translated.text)
