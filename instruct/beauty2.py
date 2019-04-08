from requests import get
import json
from bs4 import BeautifulSoup

final = []
errors = []
file_name = 'technology'

with open(file_name+'4_scrap.json') as json_file:  
    data = json.load(json_file)
    for p in range(0, len(data)):
        try:
            article = data[p]
            url = article['url']
            response = get(url)
            html_soup = BeautifulSoup(response.text, 'html.parser')
            print(str(p) + '.-' + url)

            article['category'] = file_name
            channel = ''
            try:
                channel = html_soup.find(class_ = 'channel').text
            except Exception as e:  
                channel = 'No channel to show'

            article['channel'] = channel

            final.append(article)

            if len(final) % 10 == 0:
                with open(file_name+'4_scrap2.json', 'w') as f:  # writing JSON object
                    json.dump(final, f)
        except Exception as e:
            print(str(p) + '.-' + data[p]['url'])
            print(e)
            errors.append(data[p]['url'])
            with open(file_name+'_error.json', 'w') as f:  # writing JSON object
                json.dump(errors, f)