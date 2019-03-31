"""Conversions: First Func. is getting all html text data into a file.
Second function is scraping the conversion Table data from a url."""

import requests
from bs4 import BeautifulSoup

# get the data; Random site I decided to use.
data = requests.get('https://startcooking.com/measurement-and-conversion-charts')
# The try block below outputs: There was a problem: 404 Client Error: Not Found
# the raise_for_status() method for a Response class object checks for get('URL') to ensure proper download.
try:
	data.raise_for_status()
except Exception as exc:
	print('There was a problem: %s' % (exc))


def all_text_data(data):
	"""Writes all info. into a txt file for use within recipe class."""
	with open('Cooking_Conv_url.txt', 'wb') as conver_chart:
		for chunk in data.iter_content(100000):
			conver_chart.write(chunk)

def scrape_html(data):
	"""Scrapes tr and th elements from html website."""
	# load data into bs4
	soup = BeautifulSoup(data.text, 'html.parser')
	# get data simply by looking for each tr/th
	data = []
	for tr in soup.find_all('tr'):
		values = [td.text for td in tr.find_all('td')]
		th = [th.text for th in tr.find_all('th')]
		if values:
			data.append(values)
		elif th:
			data.append(th)
	# Writes a string value of the entire list to each line
	with open('conv_lines.txt', 'w') as new:
		for list in data:
			new_data = str(list) + '\n'
			new.writelines(new_data)

# Last time I used them they both worked.
# all_text_data(data)
# scrape_html(data)
