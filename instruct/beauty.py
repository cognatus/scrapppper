from requests import get
import json
from bs4 import BeautifulSoup

final = []
errors = []
file_name = 'technology'

with open('all_'+file_name+'_links.json') as json_file:  
    data = json.load(json_file)
    for p in range(37237, 46546):
        try:
            url = data[p]['url']
            response = get(url)
            html_soup = BeautifulSoup(response.text, 'html.parser')
            print(str(p) + '.-' + url)

            title = ''   
            category = ''
            channel = ''

            if html_soup.find('h1', class_ = 'header-title') is not None:
                title = html_soup.find('h1', class_ = 'header-title').text
                
                try:
                    category = html_soup.find('.category').text
                    channel = html_soup.find('.channel').text
                except Exception as e:  
                    category = 'No category to show'
                    channel = 'No channel to show'
                    print('no info headers')

                intro = html_soup.find(id="intro")
                if intro is not None:
                    description = intro.find('div', class_ = 'step-body').text
                elif len(html_soup.find_all(class_ = 'collection-intro')) > 0:
                    description = html_soup.find_all(class_ = 'collection-intro')[0].text
                else:
                    description = title
                
                step_all = []

                steps = html_soup.find_all('section', class_ = 'step')            

                for i in range(1, len(steps)):
                    step = steps[i]
                    step_title = step.find('h2', class_ = 'step-title').text
                    steps_text = step.find('div', class_ = 'step-body').text
                    otro = step.find_all('img')
                    imgs = []

                    for img in otro:
                        imgs.append(img['src'])

                    step_all.append({
                        'step_title': step_title,
                        'steps_text': steps_text,
                        'step': i,
                        'step_imgs': imgs
                    })
                
                final.append({
                    'title': title,
                    'category': category,
                    'url': url,
                    'description': description,
                    'channel': channel,
                    'steps': step_all,
                    'section': file_name
                })

                if len(final) % 10 == 0:
                    with open(file_name+'6_scrap.json', 'w') as f:  # writing JSON object
                        json.dump(final, f)
            else:
                print('nel')
        except Exception as e:
            print(str(p) + '.-' + data[p]['url'])
            print(e)
            errors.append(data[p]['url'])
            with open(file_name+'6_error.json', 'w') as f:  # writing JSON object
                json.dump(errors, f)