import unittest

from url_analyzer import analyze

class TestUrlAnalyzer(unittest.TestCase):
    def test_raise_error_with_invalid_url(self):
        invalid_urls = ['invalidurl', '!!!!!', '12345']
        for invalid_url in invalid_urls:
            with self.assertRaises(ValueError):
                analyze(invalid_url)

    def test_raise_error_with_not_found_url(self):
        with self.assertRaises(ConnectionError):
            analyze('www.notttttfounddddurlll.com')

    def test_returns_url_data_successfully(self):
        fields = {'load_time': str, 'page_size': int, 'http_requests_count': int}
        data = analyze('criaway.com')
        for fieldKey, fieldType in fields.items():
            value = data.get(fieldKey)
            self.assertTrue(value)
            self.assertTrue(type(value) == fieldType)

if __name__ == '__main__':
    unittest.main()