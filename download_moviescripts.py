import requests
import csv
from tqdm import tqdm
from pathlib import Path
from bs4 import BeautifulSoup

html_folder = Path('movie_scripts_html')
text_folder = Path('movie_scripts_text')

if not html_folder.exists():
    html_folder.mkdir()
if not text_folder.exists():
    text_folder.mkdir()

with open('links.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for name_id, link in tqdm(csv_reader):
        resp = requests.get(link)
        if resp.ok:
            # store raw html file
            with open(html_folder / (name_id + '.html'), 'w') as write_file:
                write_file.write(resp.text)

            # extract and store script text
            with open(text_folder / (name_id + '.txt'), 'w') as write_file:
                soup = BeautifulSoup(resp.text, 'html.parser')
                soup = soup.pre
                if soup:
                    for child in soup.children:
                        if child.string:
                            text = child.string.replace('\x96', '-')
                            write_file.write(text)
                else:
                    print('Could not parse html file of {}'.format(name_id))
        else:
            print('Could not download {} with the attached link: {}'.format(name_id, link))
