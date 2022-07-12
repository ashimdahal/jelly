# Jelly
A chatbot that replies to romanized Nepali that is in production. 
![Alt text](static/img/demo.png?raw=true "Jelly In action")
Try Jelly [here online!](https://jellysathi.herokuapp.com).

#OR Use it locally on your machine
Start by cloning and installing the required libraries.

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
I had to squash previous 60+ commits and 7 Pull Requests into single commit to protect privacy on some of our API credentials and Database URLs. This act have blurred the immense amount of contributions from **[Anuj Khadka](https://github.com/Anuj-Khadka)** and **[Parash Bam](https://github.com/Parashbam69)**; show them some love by dropping a follow.


The chatbot used in this project is facebook blenderbot, used on huggingface API.

Special Thanks to **[Bishal](https://github.com/kbshal)** at https://github.com/kbshal  for his permission to use his anytranslate API, which I modded to use in our translation system.
