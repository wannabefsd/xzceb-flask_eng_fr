"""translator"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('Gx0eHjsabQr-t-WxK-JSB0CCYkF5jkmey4101F1_i99B')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/825b5f05-e961-4dd6-9d99-9f09fcad3869')

def english_to_french(english_text):
    """english to french"""
    translation=language_translator.translate(text=english_text, model_id="en-fr").get_result()
    return translation.get("translations")[0].get("translation")
    
def french_to_english(french_text):
    """french to english"""
    translation=language_translator.translate(text=french_text, model_id="fr-en").get_result()
    return translation.get("translations")[0].get("translation")
        