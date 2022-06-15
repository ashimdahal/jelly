#from Nepali_nlp import Unicode, Corrector
from google.cloud import translate
#text = 'ma ghar jaanchhu'
#print(Corrector().spell_correct(Unicode().unicode_word(text)))

def translate(text, source,target,project_id="jelly-352913"):

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": source,
            "target_language_code": target,
        }
    )

    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))
# source = 'en-US'
# target = 'ne'