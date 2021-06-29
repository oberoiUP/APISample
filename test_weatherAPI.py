import unittest
import pandas
from weatherAPI_functions import build_url, get_json


class TestFileName(unittest.TestCase):
    def test_build_url(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?' + \
          'units=imperial&q=Portland&appid=0b9ec521e0c913cd98a5430c6fae3baf'
        self.assertEqual(build_url('Portland',
                                   '0b9ec521e0c913cd98a5430c6fae3baf'), url)

    def test_get_json(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?' + \
          'units=imperial&q=Portland&appid=0b9ec521e0c913cd98a5430c6fae3baf'
        json = get_json(url)
        self.assertNotEqual(json, None)
        self.assertTrue(json['name'] == 'Portland')


if __name__ == '__main__':
    unittest.main()
