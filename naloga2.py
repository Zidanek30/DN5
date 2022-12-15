import requests

def get_api_data(url):
    h=requests.get(url)
    if h.status_code == 200:
        page=h.json()
    else:
        page='False'
    return page
data = get_api_data("https://jsonplaceholder.typicode.com/todos/1")
print(data)