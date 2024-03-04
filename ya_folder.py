import requests
import json


token = 'TOKEN'
url_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': 'OAuth ' + token}

def create_folder(folder_name):
    params = {'path': folder_name}
    result = requests.put(url_folder, headers=headers, params=params)
    return result.status_code

def folder_info(folder_name):
    params = {'path': folder_name}
    result = requests.put(url_folder, headers=headers, params=params)
    if result.status_code == 200:
        result_dict = json.loads(result.text)
        return result_dict.get('type')

if __name__ == '__main__':
    print(folder_info('TEST'))

