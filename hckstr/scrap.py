from selenium import webdriver
import time
import json

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path = '../chromedriver_linux64/chromedriver',chrome_options=options)
driver.get('https://www.hackster.io/projects/')

final = []

for i in range(233, 347):
    newPage = driver.get('https://www.hackster.io/projects/?difficulty=beginner&page='+str(i+1))
    time.sleep(3)
    content = driver.find_element_by_css_selector('.hckui__grid__cell.hckui__layout__flex')
    links = driver.execute_script("return document.getElementsByClassName('project_card__imageContainer__1cw7g');")

    print(i)
    for link in links:
        aux = {}
        aux['url'] = link.get_attribute('href')
        final.append(aux)
        print(aux['url'])
    with open('beginner3.json', 'w') as f:  # writing JSON object
        json.dump(final, f)