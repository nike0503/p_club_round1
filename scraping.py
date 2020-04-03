import requests
from bs4 import BeautifulSoup
import sys
import csv

if len(sys.argv) == 1:
    year = 2019 #default archives
elif len(sys.argv) == 2:
    url = str(sys.argv[1])
    if url[:44] != 'https://summerofcode.withgoogle.com/archive/' or url[48:] != '/projects/':
        print('Url not excepted')
        print('Enter url of form "https://summerofcode.withgoogle.com/archive/{year}/projects/"')
        sys.exit()
    year = int(url[44:-10])
else:
    print('Enter only one url')
    sys.exit()

URL = f"https://summerofcode.withgoogle.com/archive/{year}/projects/"
page = requests.get(URL)
html_data = BeautifulSoup(page.content, 'html.parser')

full_details = html_data.find_all('md-card', class_ = 'archive-project-card archive-project-card')
# after inspecting the webpage, we see that all the data we need from a webpage of this type(GSOC archives) is contained in the above class
if len(full_details) == 0:
    print('No data found at the given url')
    sys.exit()

full_details = [detail.text for detail in full_details]
full_details = [detail[:detail.index('\n\n\n\t\t\t')] for detail in full_details]
full_details = [detail.split('\n') for detail in full_details]
for detail in full_details[:1]:
    detail = [entry for entry in detail if entry != '']
full_details = [[entry for entry in detail if entry != ''] for detail in full_details]
full_details = [list([detail[0],detail[2][14:],detail[1]]) for detail in full_details]
# df = pd.DataFrame(full_details)
# df.to_csv(f'GSOC_archive_{year}.csv', index = False)

with open(f'GSOC_archive_{year}.csv', mode = 'w') as input_file:
    data_writer = csv.writer(input_file, delimiter = ',')

    for detail in full_details:
        data_writer.writerow(detail)
