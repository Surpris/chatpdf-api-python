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
    """
    Update the headers with the API key.

    No Parameters

    Returns
    -------
    None
    """
    _headers['x-api-key'] = API_KEY


def _validate_headers():
    """
    Validate the headers to ensure the API key is correct.

    No Parameters

    Raises
    ------
    ValueError
        If the API key in the headers does not match the expected API key.

    Returns
    -------
    None
    """
    assert _headers['x-api-key'] == API_KEY, ValueError(
        'API_KEY is not same as that used in uploading.'
    )


def upload_files(file_path_list: List[str]) -> str:
    """
    Upload files to the ChatPDF API.

    Parameters
    ----------
    file_path_list : List[str]
        List of file paths to upload.

    Returns
    -------
    str
        The source ID returned by the API.
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
    """
    Upload a URL to the ChatPDF API.

    Parameters
    ----------
    pdf_url : str
        The URL of the PDF to upload.

    Returns
    -------
    str
        The source ID returned by the API.
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


def chat(source_id: str, messages: List[Dict[str, str]], reference_sources: bool = False) -> str:
    """
    Chat with the uploaded files using the ChatPDF API.

    Parameters
    ----------
    source_id : str
        The source ID of the uploaded files.
    messages : List[Dict[str, str]]
        List of messages to send in the chat.
        each message has the following format:
        {
            "role": "user",  # "assistante", etc.
            "message": "..."
        }
    reference_sources : bool, optional
        Whether to reference sources in the chat, by default False

    Returns
    -------
    str
        The content returned by the API.
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


def start(source_id: str) -> str:
    """
    `Say hello` to the uploaded files using the ChatPDF API.
    This functions gives 

    Parameters
    ----------
    source_id : str
        The source ID of the uploaded files.
    messages : List[Dict[str, str]]
        List of messages to send in the chat.
        each message has the following format:
        {
            "role": "user",  # "assistante", etc.
            "message": "..."
        }

    Returns
    -------
    str
        The content returned by the API.
    """
    message = [
        {
            'role': 'user',
            'content': '<start>'
        }
    ]
    return chat(source_id, message, False)


def delete_files(source_ids: List[str]) -> int:
    """
    Delete the uploaded files from the ChatPDF API.

    Parameters
    ----------
    source_ids : List[str]
        List of source IDs of the files to delete.

    Returns
    -------
    int
        The status code returned by the API.
    """
    _validate_headers()
    url = 'https://api.chatpdf.com/v1/sources/delete'
    data = {'sources': source_ids}
    response = requests.post(
        url, headers=_headers, json=data,
        timeout=TIMEOUT_REQUEST_SEC
    )
    response.raise_for_status()
    return response.status_code
