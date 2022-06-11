# Jelly
A chatbot that replies to romanized Nepali.
Start by installing the required libraries.

    pip install -r requirements.txt
    
Create an account in hugging face and get the API KEY by going to [The tokens settings.](https://huggingface.co/settings/tokens)

Create the txt file for the token

	touch bot/token.txt && nano bot/token.txt
paste your token in the file.
## Credits

The chatbot used in this project is facebook blenderbot, used on huggingface API.

All the Nepali NLP related work is done by using the Nepali-nlp package by Sushil Ghimire.