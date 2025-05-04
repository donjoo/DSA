import requests



url = 'https://jsonplaceholder.typicode.com/todos/1'


response = requests.get(url)


for header,value in response.headers.items():
    print(f'{header}:{value}')

if response.status_code == 200:
    print('contet',response.content)
    print(response.json())
    data_string = response.text
    print(data_string)

else:
    print('met a error')


try:
    bad_url = "https://jsonplaceholder.typicode.com/todozzzz/1"
    res = requests.get(bad_url)
    res.raise_for_status()
except requests.exceptions.HTTPError as err:
    print("HTTP Error:", err)


