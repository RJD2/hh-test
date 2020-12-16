import unittest
import requests

from config import TOKEN, URL


class TestVacanciesMethod(unittest.TestCase):
    authorization = f"Bearer {TOKEN}"

    def test_success(self):
        headers = {'Authorization': self.authorization}
        response = requests.get(URL, headers=headers)

        assert response.status_code == 200

    def test_text_field(self):
        test_word = 'python'
        headers = {'Authorization': self.authorization}
        response = requests.get(f"{URL}?text={test_word}", headers=headers)

        assert response.status_code == 200
        assert test_word in response.json()['items'][0]['name'].lower()

    def test_empty_text_field(self):
        test_word = ''
        headers = {'Authorization': self.authorization}
        response = requests.get(f"{URL}?text={test_word}", headers=headers)

        assert response.status_code == 200

    def test_nonsense_data(self):
        test_word = 'fdgdfgfdree'
        headers = {'Authorization': self.authorization}
        response = requests.get(f"{URL}?text={test_word}", headers=headers)

        assert response.status_code == 200
        assert len(response.json()['items']) == 0

    def test_fail_auth(self):
        headers = {'Authorization': 'incorrect token'}
        response = requests.get(URL, headers=headers)

        assert response.status_code == 403

if __name__ == '__main__':
    unittest.main()
