import requests


def getRandomQuote():
	request_session = requests.Session()
	api_url = "https://api.quotable.io/quotes/random"
	response = request_session.get(url=api_url).json()

	result = f"{response[0]['content']}\n\n- <b>{response[0]['author']}</b>"

	return result