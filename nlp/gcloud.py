from google.cloud import translate
from google.cloud import translate_v2 as detect

def translate_text(text,source,target, project_id="jelly-352913"):

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

    return [t.translated_text for t in response.translations][0]
    
def detect_language(text):
    """Detects the text's language."""

    translate_client = detect.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)
    return result["language"]

if __name__=='__main__':
    source = 'en-US'
    target = 'ne'
    try:
        print(translate_text('Hello, I just got back from walking my dog',source,target))
    except:
        print('ok')

#source = 'ne'
#target = 'en-US'

# print(detect_language('kukur'))
