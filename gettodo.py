from selenium import webdriver
import time 
import json
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path = './chromedriver_linux64/chromedriver',chrome_options=options)
driver.get('https://www.instructables.com/')

final = []

with open('play.json') as json_file:  
    data = json.load(json_file)
    for p in range(0, len(data)):
        if p > 468:
            driver.get(data[p]['url'])
            print(data[p]['url'])

            title = driver.find_element_by_css_selector('.header-title').text
            category = driver.find_element_by_css_selector('.category').text
            channel = driver.find_element_by_css_selector('.channel').text
            esta =True
            i = 1
            step_all = []
            
            try:
                while(esta):
                    step = driver.find_element_by_id('step'+str(i))
                    step_title = step.find_element_by_css_selector('.step-title').text
                    steps_imgs = step.find_element_by_css_selector('.gallery-link')
                    otro = driver.execute_script("return document.getElementById('step"+str(i)+"').getElementsByClassName('gallery-link')")
                    imgs = []

                    for img in otro:
                        imgs.append(img.get_attribute('href'))
                    
                    step_all.append({
                        'step_title': step_title,
                        'step': i,
                        'imgs': imgs
                    })
                    i = i +1
            except NoSuchElementException as Exception:
                i = 1
                esta = False

            final.append({
                'title': title,
                'category': category,
                'channel': channel,
                'steps': step_all
            })
            if len(final) % 10 == 0:
                with open('play2_all.json', 'w') as f:  # writing JSON object
                    json.dump(final, f)
