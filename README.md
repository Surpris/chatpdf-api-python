# chatpdf-api-python

**NOTE: This module is unofficial.**

This module provides wrapper functions that ease the usage of the ChatPDF Backend APIs.

## References

* [ChatPDF](https://www.chatpdf.com/)
    * [ChatPDF Backend API](https://www.chatpdf.com/docs/api/backend)

## Installation

This module is NOT supposed to be published in PyPI for users to avoid mistaking this module for an official one. You can install this module in the usual ways you do from a given Git repository. One method is as follows:

```sh
pip install git+https://github.com/Surpris/chatpdf-api-python.git
```

## Examples

Please see the [examples](./examples) directory.

## Usage

### import and set API_KEY

```python
# import this module
import chatpdf_api_python as chatpdf

# set API_KEY if necessary.
# The API_KEY can be put in your OS environmental keys 'CHATPDF_API_KEY'
# prior to the import of this module.
chatpdf.API_KEY = '...'

```

### add PDF via a URL
```python
url = '...'

source_id = chatpdf.upload_url(url)
```

### add PDFs via file upload

```python
file_path_list = [
    '/path/to/your/file1.pdf',
    '/path/to/your/file2.pdf',
    ...
]

source_id = chatpdf.upload_files(file_path_list)
```

### chat: post messages

```python
messages = [
    { 'role': 'user', 'content': '...' },
    { 'role': 'user', 'content': '...' },
    ...
]
reference_sources = True

response = chatpdf.chat(source_id, messages, reference_sources=reference_sources)
```

### delete the uploaded files

```python
source_ids = [
    'source_id_1',
    'source_id_2',
    ...
]

response_code = chatpdf.delete_files(source_ids)
```

## Requirements

* Python 3.6+
    * `os`
    * `requests`
    * `typing`

## Contributions

We are welcom to your contributions for improving this module. Any reports, requests, etc. can be posted as issues. 

### Template for issues

Please use the following template when you post your reports, etc. about this module:

```
Title: ...
Background (optional): ...
Purpose of your post: ...
Detail of your post: ...
```

### Coding style

We do not set any coding style other than docstring of functions.

#### Style of docstring

We recommend you to using [the NumPy docstring style](https://numpydoc.readthedocs.io/en/latest/format.html).

## Disclaimer

This module uses a user-provided API token for ChatPDF. The users of this module are solely responsible for the handling of their own API token, and we assume no liability for any consequences resulting from such handling. Please be careful NOT to unknowingly disclose the API token. The users are solely responsible for the consequences if the use of this module, or any modified version of this module, results in the disclosure of the user's API token.
