from bot.blenderbot import *
# go to bot/blenderbot.py and insert your personal API KEY before calling or else it won't work
from nepali_unicode_converter.convert import Converter
import nepali_roman as nr
from os import environ,path

if 'GOOGLE_APPLICATION_CREDENTIALS' in environ:
    if path.exists(environ['GOOGLE_APPLICATION_CREDENTIALS']):
        from nlp.gcloud import *
    else:
        from nlp.api import *
        detect_language = detect_lang
else:
    from nlp.api import *
    detect_language = detect_lang



converter = Converter()
def get_input(text,previous_conversation=None,last_n=5):
    """
    This function takes user text, previous conversation and an integer as input
    to generate the input for the blenderbot API.
    INPUTS:
    text: user text
    previous_conversation : the collection of past_user_inputs and generated_responses.
    this is the section of the model's output. output['conversation'] should be passed here if
    you dont want to generate it manually
    
    last_n: number of last messages that the bot needs to remember

    returns i in the format of :
    {
		"inputs": {
			"past_user_inputs": [],
			"generated_responses": [],
			"text": "user input"
		},
	}
    
    """
    if previous_conversation is None:
        previous_conversation = {
            'past_user_inputs':[],
            'generated_responses':[]
            }

    i = {
        "inputs":
        {
            "past_user_inputs":list(previous_conversation['past_user_inputs'])[-last_n:],
            "generated_responses":list(previous_conversation['generated_responses'])[-last_n:],
            "text":text
        }
    }
    return i
    
def talk(text,prev_convo):
    '''
    Make the bot talk based on the given constraints,
    see get_input to understand the given parameters
    '''
    source = 'ne'
    target = 'en'

    if 'en' in asyncio.run(detect_language(text)):
        pass
    else:
        unicoded_nepali = converter.convert(text)
        text = asyncio.run(translate_text(unicoded_nepali, source, target))

    if prev_convo:
        inp = get_input(text,previous_conversation=prev_convo)
    else:
        inp = get_input(text)

    out = query(inp)
    generated_nepali = asyncio.run(translate_text(out['generated_text'], 'en', 'ne'))
    out['generated_text'] = nr.romanize_text(generated_nepali).replace('0','o')\
        .replace('tapaim','tapai')
    return out

def main():

    while True:
        inp = input('user:')
        if inp =='bye': break
        ## make input here based on the output is already generated or not
        source = 'ne'
        target = 'en-US'

        if 'en' in asyncio.run(detect_language(inp)):
            pass
        else:
            unicoded_nepali = converter.convert(inp)
            inp = asyncio.run(translate_text(unicoded_nepali, source, target))
        if 'out' in locals():
            i = get_input(inp,previous_conversation = out['conversation'])
       
        else:
            i = get_input(inp)
        out = query(i)
        nepali_out = asyncio.run(translate_text(out['generated_text'], 'en-US', 'ne'))
        print('bot: ',nr.romanize_text(nepali_out))

if __name__ == '__main__':
    main()