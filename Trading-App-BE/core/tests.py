from django.test import TestCase
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

class AlphaVantageAPITest(TestCase):
    def test_api(self):
        api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        symbol = 'TSCO.LON'
        function = 'TIME_SERIES_DAILY'
        outputsize = 'full'

        url =f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={outputsize}&apikey={api_key}'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

        data = response.json()

        with open('alpha_vantage_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        self.assertIn('Meta Data', data)
        self.assertIn('Time Series (Daily)', data)
