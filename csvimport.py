import urllib.request
import os


if os.path.exists('/Users/AYUSH/Downloads/covid.csv'):
   os.remove('/Users/AYUSH/Downloads/covid.csv')

print('Beginning file download with urllib2...')
url = 'https://covid.ourworldindata.org/data/full_data.csv'
urllib.request.urlretrieve(url, '/Users/AYUSH/Downloads/covid.csv')

