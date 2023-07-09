"""chatpdf_api_python.main
"""

from typing import List, Dict
import os
import requests

API_KEY = os.environ.get('CHATPDF_API_KEY', '')
TIMEOUT_REQUEST_SEC = 30.0

_headers = {
    'x-api-key': API_KEY,
}


def _update_headers():
    _headers['x-api-key'] = API_KEY


def _validate_headers():
    assert _headers['x-api-key'] == API_KEY, ValueError(
        'API_KEY is not same as that used in uploading.'
    )


def upload_files(file_path_list: List[str]) -> str:
    """upload files 
    """
    _update_headers()
    url = 'https://api.chatpdf.com/v1/sources/add-file'
    files = [
        ('file', ('file', open(file_path, 'rb'), 'application/octet-stream'))
        for file_path in file_path_list
    ]

    response = requests.post(
        url, headers=_headers, files=files,
        timeout=TIMEOUT_REQUEST_SEC
    )
    if response.status_code != 200:
        error_message = 'status code: {0}, message: {1}'.format(
            response.status_code,
            response.text
        )
        raise requests.exceptions.HTTPError(error_message)

    return response.json()['sourceId']


def upload_url(pdf_url: str) -> str:
    """upload a url
    """
    _update_headers()
    url = 'https://api.chatpdf.com/v1/sources/add-url'
    data = {'url': pdf_url}

    response = requests.post(
        url, headers=_headers, json=data,
        timeout=TIMEOUT_REQUEST_SEC
    )
    if response.status_code != 200:
        error_message = 'status code: {0}, message: {1}'.format(
            response.status_code,
            response.text
        )
        raise requests.exceptions.HTTPError(error_message)

    return response.json()['sourceId']


def chat(source_id: str, messages: List[Dict[str, str]], reference_sources: bool = False):
    """chat with the uploaded files
    """
    _validate_headers()
    url = 'https://api.chatpdf.com/v1/chats/message'
    data = {
        'referenceSources': reference_sources,
        'sourceId': source_id,
        'messages': messages,
    }
    response = requests.post(
        url, headers=_headers, json=data,
        timeout=TIMEOUT_REQUEST_SEC
    )
    if response.status_code != 200:
        error_message = 'status code: {0}, message: {1}'.format(
            response.status_code,
            response.text
        )
        raise requests.exceptions.HTTPError(error_message)
    return response.json()['content']


def delete_files(source_ids: List[str]):
    """delete the uploaded files
    """
    _validate_headers()
    url = 'https://api.chatpdf.com/v1/sources/delete'
    data = {'sources': source_ids}
    response = requests.post(
        url, headers=_headers, json=data,
        timeout=TIMEOUT_REQUEST_SEC
    )
    return response.status_code
