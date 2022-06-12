import requests
token = open('/home/parashbam16/anaconda3/envs/jellyproject/chatbot/jelly/bot/token.txt').read()
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer {token}"}

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
