import json, requests, ctypes

"""
token from https://github.com/Snbig/InstaTrack
"""
def usernameExists(user):
    r = requests.get('https://www.instagram.com/web/search/topsearch/?query=' + user, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}).text

    if json.loads(r).get("message") == 'rate limited':
        print(
            '[x] Rate limit reached!\n[#] Unchecked Username: {}\n[!] Try again in a few minutes.\n'.format(user))
        exit()

    try:
        for i in range(len(json.loads(r)['users'])):
            if json.loads(r)['users'][i]['user']['username'] == user:
                return json.loads(r)['users'][i]['user']['pk']
    except IndexError:
        return False



def main():

    usernamesToCheck = ["john", "johnsmith", "john_smith"]
    avaliableUsernames = []

    for username in usernamesToCheck:
        id = usernameExists(username)
        if not id:
            avaliableUsernames.append(username)
    
    print ("Avaliable Username(s):")
    print (avaliableUsernames)

if __name__ == '__main__':
    main()