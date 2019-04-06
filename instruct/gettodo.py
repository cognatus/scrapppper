from selenium import webdriver
import time 
import json
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path = '../chromedriver_linux64/chromedriver',chrome_options=options)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)

final = []
errors = []
file_name = 'home'

with open('all_'+file_name+'_links.json') as json_file:  
    data = json.load(json_file)
    print(len(data))
    for p in range(0, len(data)):
        try:
            driver.get(data[p]['url'])
            wait.until(EC.visibility_of_element_located((By.ID, "instructables-logo")))
            print(str(p) + '.-' + data[p]['url'])
            url = data[p]['url']
            title = ''   
            category = ''
            channel = ''
            pasa = True
            try:
                title = driver.find_element_by_css_selector('.header-title').text
            except NoSuchElementException as Exception:
                pasa = False        
                print('no info')
            if pasa:
                try:
                    category = driver.find_element_by_css_selector('.category').text
                    channel = driver.find_element_by_css_selector('.channel').text
                except NoSuchElementException as Exception:  
                    print('no info headers')
                description = ''
                try:
                    description = driver.execute_script("var intro = document.getElementById('intro'); return intro ? intro.getElementsByClassName('step-body')[0] : (document.getElementsByClassName('collection-intro').length > 0 ? document.getElementsByClassName('collection-intro')[0] : document.getElementsByClassName('header-title')[0])").text
                except Exception as e:
                    description = 'No description available'
                esta =True
                i = 1
                step_all = []
                try:
                    while(esta):
                        step = driver.find_element_by_id('step'+str(i))
                        step_title = step.find_element_by_css_selector('.step-title').text
                        steps_text = step.find_element_by_css_selector('.step-body').text
                        otro = driver.execute_script("return document.getElementById('step"+str(i)+"').getElementsByClassName('gallery-link')")
                        imgs = []

                        for img in otro:
                            imgs.append(img.get_attribute('href'))
                        
                        step_all.append({
                            'step_title': step_title,
                            'steps_text': steps_text,
                            'step': i,
                            'step_imgs': imgs
                        })
                        i = i +1
                except:
                    i = 1
                    esta = False

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
                    with open(file_name+'_scrap.json', 'w') as f:  # writing JSON object
                        json.dump(final, f)
        except:
            errors.append(data[p]['url'])
            with open(file_name+'_error.json', 'w') as f:  # writing JSON object
                json.dump(errors, f)

driver.close()