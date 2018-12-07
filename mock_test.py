import requests
import requests_mock


class TestClass(object):
    def test_mock(self):
        with requests_mock.Mocker() as m:
            m.get('http://dlp.com', text='dlp_resp')
            resp=requests.get('http://dlp.com').text
            return resp
            #assert requests.get('http://dlp.com').text == 'dlp_resp'


resp = TestClass().test_mock()
print(resp)