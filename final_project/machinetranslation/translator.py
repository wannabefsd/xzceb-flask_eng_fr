"""translator"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('8DyvK10Mb1D33mxY_tQIUaYgT5NokbHPDp-DlSg0rV85')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/d9a2981b-9603-40df-93ae-45f9d897efe3')

def english_to_french(english_text):
    """english to french"""
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translation']
    print(translation)
    return french_text

def french_to_english(french_text):
    """french to english"""
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translation']
    print(translation)
    return english_text
