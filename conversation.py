from bot.blenderbot import *
# go to bot/blenderbot.py and insert your personal API KEY before calling or else it won't work

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
        print(True)

    i = {
        "inputs":
        {
            "past_user_inputs":list(previous_conversation['past_user_inputs'])[-last_n:],
            "generated_responses":list(previous_conversation['generated_responses'])[-last_n:],
            "text":text
        }
    }
    return i

def main():

    while True:
        inp = input('user:')
        if inp =='bye': break
        ## make input here based on the output is already generated or not
        if 'out' in locals():
            i = get_input(inp,previous_conversation = out['conversation'])
       
        else:
            i = get_input(inp)
        out = query(i)
        print('bot: ',out['generated_text'])

if __name__ == '__main__':
    main()