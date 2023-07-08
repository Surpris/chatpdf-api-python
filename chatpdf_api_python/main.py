import os
import requests
from typing import List, Dict

API_KEY = os.environ.get('CHATPDF_API_KEY', '')

_headers = {
    'x-api-key': API_KEY,
}


def _update_headers():
    _headers['x-api-key'] = API_KEY


def _validate_headers():
    assert _headers['x-api-key'] == API_KEY, ValueError(
        'API_KEY is not same as that used in uploading.'
    )


def upload_file(file_path_list: List[str]) -> str:
    _update_headers()
    url = 'https://api.chatpdf.com/v1/sources/add-file'
    files = [
        ('file', ('file', open(file_path, 'rb'), 'application/octet-stream'))
        for file_path in file_path_list
    ]

    response = requests.post(url, headers=_headers, files=files)
    if response.status_code == 200:
        return response.json()['sourceId']
    else:
        raise Exception(f"status code: {response.status_code}, message: {response.text}")


def upload_url(pdf_url: str) -> str:
    _update_headers()
    url = 'https://api.chatpdf.com/v1/sources/add-url'
    data = {'url': pdf_url}

    response = requests.post(url, headers=_headers, json=data)
    if response.status_code == 200:
        return response.json()['sourceId']
    else:
        raise Exception(f"status code: {response.status_code}, message: {response.text}")
    return response.json()


def send_receive_message(source_id: str, messages: List[Dict[str, str]], reference_sources: bool = False):
    _validate_headers()
    url = 'https://api.chatpdf.com/v1/chats/message'
    data = {
        'referenceSources': reference_sources,
        'sourceId': source_id,
        'messages': messages,
    }
    response = requests.post(url, headers=_headers, json=data)
    return response.json()['content']


def delete_file(source_ids: str):
    _validate_headers()
    url = 'https://api.chatpdf.com/v1/sources/delete'
    data = {'sources': source_ids}
    response = requests.post(url, headers=_headers, json=data)
    return response.status_code
