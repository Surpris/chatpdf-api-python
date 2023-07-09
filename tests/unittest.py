import os
import unittest
from your_module import upload_files, upload_url, chat, delete_files


class TestChatPdfApi(unittest.TestCase):
    def setUp(self):
        self.api_key = os.environ['CHATPDF_API_KEY']
        self.test_file_path = 'path_to_your_test_file.pdf'
        self.test_url = 'https://example.com/test.pdf'

    def test_upload_file(self):
        response = upload_file(self.test_file_path)
        self.assertTrue(isinstance(response, str))

    def test_upload_url(self):
        response = upload_url(self.test_url)
        self.assertTrue(isinstance(response, str))

    def test_send_receive_message(self):
        source_id = 'your_source_id'
        messages = [{'role': 'user', 'content': 'couild you summarize the contents of the uploaded PDF?'}]
        response = chat(source_id, messages)
        self.assertTrue(isinstance(response, str))

    def test_delete_file(self):
        source_ids = ['your_source_id']
        status_code = delete_files(source_ids)
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()
