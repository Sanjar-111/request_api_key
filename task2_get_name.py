import requests

key={'X-Api-Key': "549a3b2da12a434f9f5eb843eb7a2933"}


def get_random_name(api_key:str,nameType:str, quantity: int):
    """
    Make a GET request to the Randommer API to get a random name.

    This function should:
    - Send a GET request to: https://randommer.io/api/Name
    - With parameter nameType and quantity
    - nameType = one of these ("firstname" "surname" "fullname")
    - quantity = number of names
    - Include the API key in the X-Api-Key header
    - Print the random name from the response
    """
    x={
        'nameType': nameType,
        'quantity': quantity
    }
    card=requests.get('https://randommer.io/api/Name',headers=key,params=x)
    return card.json()
print(get_random_name(nameType="firstname",quantity=5,api_key=key))
