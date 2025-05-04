import requests

url = 'https://api.github.com/users/donjoo'

response = requests.get(url)


if response.status_code == 200:
    user_info = response.json()
    print(user_info)
    print(f"User:  {user_info['login']}")
    print(f"name: {user_info['name']}")
    print(f"Public repos : {user_info['public_repos']}")

else:
        print('failed to extract datas')