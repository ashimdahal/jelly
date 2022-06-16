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
# source = 'ne'
# target = 'en-US'

# inp = converter.convert('mero kukur xa')
# print(translate_text('how are you doing',source,target))
# print(detect_language('kukur'))