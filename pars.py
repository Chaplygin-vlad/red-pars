from selenium import webdriver
def check_exists_by_xpath(xpath):
    return len(driver.find_elements_by_xpath(xpath)) > 0
#from selenium.webdriver.common.keys import Keys
urls=[]
driver = webdriver.Firefox()
driver.get('https://www.reddit.com/search/?q=план маршала')
news=driver.find_elements_by_xpath("//a[@class='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE']")
b=1
c = 1
for i in news[:5]:
    a=i.get_attribute('href')
    url= {
        'href': a
    }
    urls.append(url)
for j in urls:
    driver.get(j['href'])
    ttl=driver.find_element_by_xpath("//h1[@class='_eYtD2XCVieq6emjKBH3m']")
    #com=driver.find_elements_by_xpath("//p[@class='_1qeIAgB0cPwnLhDF9XSiJM']")
    com=driver.find_elements_by_xpath("//div[@class='_3tw__eCCe7j-epNCKGXUKk ']/div/div/p")
    pic_check=check_exists_by_xpath("//div[@class='_3Oa0THmZ3f5iZXAQ0hBJ0k ']//a")
    lnk_check=check_exists_by_xpath("//a[@class='_13svhQIUZqD9PVzFcLwOKT styled-outbound-link']")
    com_check=check_exists_by_xpath("//div[@class='_3tw__eCCe7j-epNCKGXUKk ']/div/div/p")
    txt_check=check_exists_by_xpath("//div[@data-click-id='text']/div/p")
    print ("Заголовок"+str(b)+": "+ttl.text)
    if pic_check > 0:
        pic=driver.find_element_by_xpath("//div[@class='_3Oa0THmZ3f5iZXAQ0hBJ0k ']//a")
        print (pic.get_attribute('href'))
    else:
        print ("Изображений нет")
    if lnk_check > 0:
        lnk=driver.find_element_by_xpath("//a[@class='_13svhQIUZqD9PVzFcLwOKT styled-outbound-link']")
        print (lnk.get_attribute('href'))
    else:
        print ("Ссылок нет")
    if txt_check > 0:
        txt=driver.find_elements_by_xpath("//div[@data-click-id='text']/div/p")
        for f in txt:
            print(f.text)
    else:
        print("Текст поста отсутствует")
    if com_check > 0:
        c=1
        for h in com[:5]:
            print ("Комментарий " +str(c)+": "+h.text)
            c=c+1
    else:
        print ("Комментарии отсутсвуют")
    print ("\n \n \n")
    b+=1


#_13svhQIUZqD9PVzFcLwOKT styled-outbound-link - a класс где ссылка в теле
#<div class="_3Oa0THmZ3f5iZXAQ0hBJ0k - div класс где картинка


