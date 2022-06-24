import requests,os
try:
	token = open(os.path.join('bot','token.txt')).read()
except:
	pass
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": f"Bearer {token}"}
def query(payload):
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
