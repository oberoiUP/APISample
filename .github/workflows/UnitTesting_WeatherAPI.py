import unittest
from test_weatherAPI import build_url, get_json

class TestFileName(unittest.TestCase):
    def test_build_url(self):
        self.assertEqual(build_url('Portland', '0b9ec521e0c913cd98a5430c6fae3baf'), 'https://api.openweathermap.org/data/2.5/weather?units=imperial&q=Portland&appid=0b9ec521e0c913cd98a5430c6fae3baf')
    
    def test_get_json(self):
        json = get_json('https://api.openweathermap.org/data/2.5/weather?units=imperial&q=Portland&appid=0b9ec521e0c913cd98a5430c6fae3baf')
        self.assertNotEqual(json, NULL)
        self.assertTrue(json['name'] == 'Portland')
    
if __name__ == '__main__':
    unittest.main()