from selenium import webdriver
import time
import json

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path = './chromedriver_linux64/chromedriver',chrome_options=options)
driver.get('https://www.instructables.com/outside/')

pagination = driver.find_element_by_css_selector('.pull-right.pagination')
pages = pagination.find_elements_by_xpath('.//li')
numberPages = int(pages[len(pages)-2].text)
final = []

for i in range(0, numberPages):
    newPage = driver.get('https://www.instructables.com/outside/?offset='+str(i*59))
    articleList = driver.find_element_by_css_selector('.explore-covers-list.clearfix').find_elements_by_xpath('.//li')
    for article in articleList:
        aux = {}
        element = article.find_element_by_css_selector('.title')
        aux['title'] = element.text
        aux['url'] = element.find_element_by_xpath('.//a').get_attribute('href')
        final.append(aux)
    print(str((i+1)*59)+' articles read')
    if (i+1)*59 > 10000:
        with open('outside.json', 'w') as f:  # writing JSON object
            json.dump(final, f)
        break