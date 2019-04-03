from selenium import webdriver
import time 
import json
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path = '../chromedriver_linux64/chromedriver',chrome_options=options)
driver.get('https://www.hackster.io/')

time.sleep(1)
driver.find_element_by_css_selector('.hckui__typography__linkBlue').click()
time.sleep(2)
driver.execute_script("return document.getElementById('email_address_email')").send_keys('diegojmartinezzm@gmail.com')
driver.execute_script("return document.getElementById('password_password')").send_keys('hola1234')
#loginmodal.find_element_by_id('password_password').sendKeys('hola1234')
time.sleep(1)
driver.execute_script("return document.querySelectorAll('.hckui__buttons__lg.undefined.hckui__layout__fullWidth')[0]").click()
print('Logged')
time.sleep(5)
print('This shit just started')

final = []

category = 'intermediate2'

with open(category+'.json') as json_file:  
    data = json.load(json_file)
    for p in range(0, len(data)):
        driver.get(data[p]['url'])
        print(str(p) + '.-' + data[p]['url'])
        url = data[p]['url']
        title = ''
        pasa = True
        try:
            title = driver.find_element_by_css_selector('h1').text
        except NoSuchElementException as Exception:
            pasa = False        
            print('no info')
        if pasa:
            #intro = driver.find_element_by_id('intro')
            description = ''
            try:
                description = driver.execute_script("var overview = document.getElementById('overview'); return overview ? overview.getElementsByTagName('p')[0] : document.getElementsByTagName('h1')[0]").text
            except Exception as e:
                description = 'No description available'
            
            materials_list = driver.execute_script("return document.querySelectorAll('td.hckui__typography__bodyL:not(.times):not(.quantity)')")
            materials = []
            for material in materials_list:
                materials.append({
                    'material': material.text
                })

            story = ''
            try:
                story = driver.find_element_by_id("story").get_attribute('innerHTML')
            except NoSuchElementException as Exception:
                story = '<p>No Story for this article</p>'

            final.append({
                'title': title,
                'category': category,
                'url': url,
                'description': description,
                'body': story,
                'materials': materials
            })
            if len(final) % 10 == 0:
                with open(category+'_all.json', 'w') as f:  # writing JSON object
                    json.dump(final, f)

