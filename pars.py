from selenium import webdriver
from flask import Flask
import postgres



app = Flask(__name__)

@app.route('/')
def main_page():
    return ('Приложение для парсинга Reddit.com')

@app.route('/<post_name>')
def parsing_reddit(post_name):
    urls = []
    driver = webdriver.Firefox()
    driver.get('https://www.reddit.com/search/?q=' + post_name)
    news = driver.find_elements_by_xpath("//a[@class='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE']")
    all_text = []
    comments = []
    postgres.drop_sql()
    postgres.create_sql()
    for i in news[:5]:
        a = i.get_attribute('href')
        url = {
            'href': a
        }
        urls.append(url)
    for j in urls:
        driver.get(j['href'])
        try:
            header = driver.find_element_by_xpath("//h1[@class='_eYtD2XCVieq6emjKBH3m']").text
        except Exception:
            header = ' '
        try:
            image = driver.find_element_by_xpath("//div[@class='_3Oa0THmZ3f5iZXAQ0hBJ0k ']//a").get_attribute('href')
        except Exception:
            image = 'Изображение отсутсвует'
        try:
            news_link = driver.find_element_by_xpath(
                "//a[@class='_13svhQIUZqD9PVzFcLwOKT styled-outbound-link']").get_attribute('href')
        except Exception:
            news_link = 'Ссылка на внешний источник отсутсвует'
        try:
            text = driver.find_elements_by_xpath("//div[@data-click-id='text']/div/p")
            for i in text:
                all_text.append(i.text)
            if all_text == []:
                all_text = 'Текст поста отсутствует'
        except Exception:
            all_text = 'Текст поста отсутсвует'
        try:
            comment = driver.find_elements_by_xpath("//div[@class='_3tw__eCCe7j-epNCKGXUKk ']/div/div/p")
            for i in comment[0:5]:
                comments.append(i.text)
            if comments == []:
                comments = 'Комментарии отсутсвуют'
        except Exception:
            comments = 'Комментарии отсутсвуют'

        data = {'header': header,
                'image': image,
                'news_link': news_link,
                'all_text': all_text,
                'comments': comments,
                }
        # print(data)
        all_text = []
        comments = []
        postgres.write_pstgres(data)
    driver.quit()
    return 'Парсинг Reddit завершен'


if __name__ == '__main__':
    app.run(debug=True)

