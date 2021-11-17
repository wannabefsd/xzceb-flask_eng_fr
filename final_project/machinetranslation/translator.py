"""translator"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/825b5f05-e961-4dd6-9d99-9f09fcad3869')

def englishToFrench(englishText):
    """english to french"""
    translation = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText=translation['translations'][0]['translation']
    print(translation)
    return frenchText
    
def frenchToEnglish(frenchText):
    """french to english"""
    translation = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    englishText=translation['translations'][0]['translation']
    print(translation)
    return englishText
