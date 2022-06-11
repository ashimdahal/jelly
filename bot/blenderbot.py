import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer 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"}

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
