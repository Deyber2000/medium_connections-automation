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
    print('Retrieving users from Followings...')
    next_id = False
    followings = []
    while True:
        if next_id: # If this is not the first page of the followings list
            url = MEDIUM + '/_/api/users/' + user_id + '/following?limit=8&to=' + next_id
        else: # If this is the first page of the followings list
            url = MEDIUM + '/_/api/users/' + user_id + '/following'
        response = requests.get(url)
        response_dict = clean_json_response(response)
        payload = response_dict['payload']
        for user in payload['value']:
            followings.append(user['username'])
        try:
            next_id = payload['paging']['next']['to']
        except:
            break
        return followings
def get_list_of_latest_posts_ids(usernames):
    print('Retrieving the latest posts...')
    post_ids = []
    for username in usernames:
        url = MEDIUM + '/@' + username + '/latest?format=json'
        response = requests.get(url)
        response_dict = clean_json_response(response)
        try:
            posts = response_dict['payload']['references']['Post']
        except:
            posts = []
        if posts:
            for key in posts.keys():
                post_ids.append(posts[key]['id'])
        return post_ids