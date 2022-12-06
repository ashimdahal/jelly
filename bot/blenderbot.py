import requests,os

try:
	token = open(os.path.join('bot','token.txt')).read()
except:
	print('no token file')

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
def query(payload,headers):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

if __name__ == '__main__':
	i = {
		"inputs": {
			"past_user_inputs": [],
			"generated_responses": [],
			"text": "Hello"
		},
	}
	output = query(i)
	print(output)
