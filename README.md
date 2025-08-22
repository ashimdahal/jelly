# Jelly

Jelly is the one and only chatbot in existence that replies to romanized Nepali. The chatbot is currently in production and can be used online or locally on your own machine.

![Alt text](static/img/demo.png?raw=true "Jelly In action")

- Try Jelly demo from --- Jelly has been discontinued because of advents of ChatGPT. You can still try by compiling it and read our research paper.

- Read the research about jelly from [here](https://www.researchsquare.com/article/rs-2183870/v2)

## Description
Jelly is a chatbot that uses natural language processing to understand and reply to romanized Nepali. It is built using the Facebook BlenderBot, which is available through the huggingface API.

To use Jelly locally on your machine, start by cloning the repository and installing the required libraries:

```
git clone https://github.com/ashimdahal/jelly.git 
cd jelly/
pip install -r requirements.txt
```

Next, [OPTIONAL] create an account on huggingface and obtain an API KEY by going to the [tokens settings](https://huggingface.co/settings/tokens). You will be asked to enter the API key when you run the app but can enter anything to run the app temporarily.

To run the app using Flask, set the environment variable and run the Flask app:

```
export FLASK_APP=index
flask run
```

Or Just run it the following way:

```
python app.py
```

---

## Credits

In order to protect the privacy of certain API credentials and database URLs, we had to squash previous commits (60+ in total) into a single commit. This means that the commit history of this project does not accurately reflect the full extent of the contributions made by our collaborators [Anuj Khadka](https://github.com/Anuj-Khadka) and [Parash Bam](https://github.com/Parashbam69). We would like to extend our thanks to them for their hard work and dedication to this project.

Special thanks to [Bishal](https://github.com/kbshal) for allowing us to use his [anytranslate](https://github.com/kbshal/Anytranslate) API in our translation system.

The chatbot used in this project is facebook blenderbot, used on huggingface API.
