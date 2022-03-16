import services.util_service as us
import requests
import html
import json

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}

config = us.getConfig()

def get_html(source):
    r = requests.get(source,headers=headers)
    return html.unescape(r.text)

def get_data(day):
    url = f'{config.get("DATA_SOURCE")}{day}/'
    r = requests.get(url,headers=headers)
    text = r.text
    json_obj = json.loads(text)
    return json_obj.get('TorikumiData')

def get_list_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')
        return json.loads(data)

