# Jelly
A chatbot that replies to romanized Nepali that is production ready. Start by cloning and installing the required libraries.

    git clone https://github.com/ashimdahal/jelly.git
	pip install -r requirements.txt     
  Create an account in hugging face and get the API KEY by going to [the tokens settings.](https://huggingface.co/settings/tokens)

You'd be asked to paste the token when you run the app.
## Run it using FLASK
Set the environment variable and run the flask app.
```
export FLASK_APP=index
flask run
```

## Credits

The chatbot used in this project is facebook blenderbot, used on huggingface API.

Special Thanks to **[Bishal](https://github.com/kbshal)** at https://github.com/kbshal  for his permission to use his anytranslate API, which I modded to use in our translation system.
