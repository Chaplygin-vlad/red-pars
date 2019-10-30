from selenium import webdriver

#from selenium.webdriver.common.keys import Keys
urls=[]
driver = webdriver.Firefox()
driver.get('https://www.reddit.com/search/?q=москва')
news=driver.find_elements_by_xpath("//a[@class='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE']")
for i in news[:5]:
    a=i.get_attribute('href')
    url= {
        'href': a
    }
    urls.append(url)
for j in urls:
    driver.get(j['href'])
    ttl=driver.find_element_by_xpath("//h1[@class='_eYtD2XCVieq6emjKBH3m']")
    com=driver.find_elements_by_xpath("//p[@class='_1qeIAgB0cPwnLhDF9XSiJM']")
    print (ttl.text)
    print (com[:5]) #ищет пока просто элементы

