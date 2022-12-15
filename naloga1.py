import requests

def get_html(url):
    h=requests.get(url)
    if h.status_code == 200:
        page=h.text
    else:
        page='False'
    return page
page = get_html("http://example.com/neobstaja")
print(page)