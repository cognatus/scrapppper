from selenium import webdriver
import time
import json

category = 'outside'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path = './chromedriver_linux64/chromedriver',chrome_options=options)
driver.get('https://www.instructables.com/'+category+'/')

pagination = driver.find_element_by_css_selector('.pull-right.pagination')
pages = pagination.find_elements_by_xpath('.//li')
numberPages = int(pages[len(pages)-2].text)
final = []

for i in range(0, numberPages):
    newPage = driver.get('https://www.instructables.com/'+category+'/?offset='+str(i*59))
    articleList = driver.find_element_by_css_selector('.explore-covers-list.clearfix').find_elements_by_xpath('.//li')
    for article in articleList:
        aux = {}
        aux['url'] = element.find_element_by_xpath('.//a').get_attribute('href')
        final.append(aux)
    print(str(i)+'.-'+str(i*59))
    if (i+1) % 10 == 0:
        with open(category+'_links.json', 'w') as f:
            json.dump(final, f)
        print('Saved at index '+str(i))
