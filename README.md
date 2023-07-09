# chatpdf-api-python

**This module is unofficial.**

Python wrapper for [ChatPDF Backend API](https://www.chatpdf.com/docs/api/backend){:target="_blank"}. This module provides wrapper functions that ease usage of ChatPDF APIs.

## References

* [ChatPDF](https://www.chatpdf.com/)
    * [ChatPDF Backend API](https://www.chatpdf.com/docs/api/backend)

# Installation

This module is NOT supposed to be published in PyPi to avoid mistaking this module for an official one. You can install this module in the usual ways you do from a given Git repository. One method is as follows:

```sh
pip install git+https://github.com/Surpris/chatpdf-api-python.git
```

# Examples

Please see the [examples](./examples) directory.

# Usage

## import and set API_KEY

```python
# import this module
import chatpdf_api_python as chatpdf

# set API_KEY if necessary.
# The API_KEY can be put in your OS environmental keys 'CHATPDF_API_KEY'
# prior to the import of this module.
chatpdf.API_KEY = '...'

```

## add PDF via a URL
```python
url = '...'

source_id = chatpd.upload_url(url)
```

## add PDFs via file upload

```python
file_path_list = [
    '/path/to/your/file1.pdf',
    '/path/to/your/file2.pdf',
    ...
]

source_id = chatpdf.upload_files(file_path_list)
```

## post messages

```python
messages = [
    { 'role': 'user', 'content': '...' },
    { 'role': 'user', 'content': '...' },
    ...
]
reference_sources = True

response = chatpdf.chat(source_id, messages, reference_sources=reference_sources)
```

## delete the uploaded files

```python
source_ids = [
    'source_id_1',
    'source_id_2',
    ...
]

response_code = chatpdf.delete_files(source_ids)
```

# Requirements

No special Python modules are required. This module imports the followings:

* `os`
* `requests`

# Tested Python version

* Python 3.10
