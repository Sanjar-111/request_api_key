import requests

key={'X-API-KEY': "549a3b2da12a434f9f5eb843eb7a2933"}


def get_random_card(key):
    """
    Make a GET request to the Randommer API to get a random card.

    This function should:
    - Send a GET request to: https://randommer.io/api/Card
    - Include the API key in the X-Api-Key header
    - Print the response JSON containing card information
    """
    card=requests.get('https://randommer.io/api/Card',headers=key)
    return card.json()['cardNumber']
print(get_random_card(key))