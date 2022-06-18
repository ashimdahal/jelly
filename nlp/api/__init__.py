try:
    from PYtranslator import *
except:
    from .PYtranslator import *

package = google_translator()

async def translate_text(text,source,target):
    """
    Translates the given text using PYtranslator's google translator.
    """
    
    translated = await package.translate(text,lang_src=str(source),lang_tgt=str(target))
    return translated

async def detect_lang(text):
    """
    returns the detected language using langdetect library
    """
    return await package.detect(text)

if __name__=="__main__":
    # print(asyncio.run(translate_text('Hi! I just got back from walking my dog.', 'en', 'ne')))
    print('en' in asyncio.run(detect_lang('Hi! I just got back from walking my dog.')))