# Jelly
A chatbot that replies to romanized Nepali. Start by cloning and installing the required libraries.

    git clone https://github.com/ashimdahal/jelly.git
	pip install -r requirements.txt     
  Create an account in hugging face and get the API KEY by going to [the tokens settings.](https://huggingface.co/settings/tokens)

Create the txt file for the token

	touch bot/token.txt && nano bot/token.txt
paste your token in the file.

In order to get proper translation from English to Nepali and vice-versa, follow the [google cloud authentication process](https://cloud.google.com/docs/authentication/getting-started) and get the key.json file to run the project. We don't provide the google cloud key for privacy reasons.
## Run it using FLASK
Set the environment variable and run the flask app.
```
export FLASK_APP=index
flask run
```

## Credits

The chatbot used in this project is facebook blenderbot, used on huggingface API.

All the Nepali NLP related work is done by using the Nepali-nlp package by Sushil Ghimire.