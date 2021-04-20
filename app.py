import request
import json

MEDIUM = 'https://medium.com'

def clean_json_response(response):
    return json.loads(response.text.split('])}while(1);</x>')[1])
def get_user_id(username):
    print('Retrieving user ID...')
    url = MEDIUM + '/@' + username + '?format=json'
    response = requests.get(url)
    response_dict = clean_json_response(response)
    return response_dict['payload']['user']['userId']

def get_list_of_followings(user_id):
    
