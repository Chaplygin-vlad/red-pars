from selenium import webdriver
from sanic import Sanic
from sanic.response import text
import postgres
import Path


def sanic_start():

    app = Sanic()

    @app.route("/")
    async def main_page(request):
        return text('Приложение для парсинга Reddit.com.  Добавьте к адресной строке "/search/<ваш запрос>" для поиска')


    @app.route('/search/<post_name>')
    async def parsing_reddit(request, post_name):
        urls = []
        driver = webdriver.Firefox()
        driver.get('https://www.reddit.com/search/?q=' + post_name)
        news = driver.find_elements_by_xpath(Path.news_xpath)
        comments = []
        #index = 1
        #postgres.drop_sql()
        #postgres.create_sql()
        for i in news[:5]:
            a = i.get_attribute('href')
            url = {
                'href': a
                }
            urls.append(url)
        for j in urls:
            driver.get(j['href'])

            try:
                header = driver.find_element_by_xpath(Path.header_xpath).text
            except Exception:
                header = ' '
            try:
                image = driver.find_element_by_xpath(Path.image_xpath).get_attribute('href')
            except Exception:
                image = 'Изображение отсутсвует'
            try:
                news_link = driver.find_element_by_xpath(Path.news_link_xpath).get_attribute('href')
            except Exception:
                news_link = 'Ссылка на внешний источник отсутсвует'

            try:
                description = driver.find_element_by_xpath(Path.description_xpath).text
            except Exception:
                description = 'Текст поста отсутсвует'

            try:
                driver.find_element_by_xpath(Path.sort_button_xpath).click()
                driver.implicitly_wait(4)
                driver.find_element_by_xpath(Path.sort_1_button_xpath).click()
                driver.implicitly_wait(4)
            except Exception:
                print()
            try:
                driver.find_element_by_xpath(Path.comment_unpack_button_xpath).click()
            except Exception:
                print()

            try:
                comment = driver.find_elements_by_xpath(Path.comment_xpath)
                for id, i in enumerate(comment[0:5]):
                    id += 1
                    comments.append((str(id) + '.Comment: ' + i.text))
                if comments == []:
                    comments = 'Комментарии отсутсвуют'
            except Exception:
                comments = 'Комментарии отсутсвуют'

            data = {
                    'header': header,
                    'image': image,
                    'news_link': news_link,
                    'description': description,
                    'comments': comments,
                    }
            # print(data)
            comments = []
            #index +=1
            postgres.write_pstgres(data)
        driver.quit()
        return text('Парсинг Reddit завершен')

    app.run(debug=True)

# if __name__ == '__main__':
#     app.run(debug=True)

