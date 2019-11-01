from selenium import webdriver
import psycopg2


def write_pstgres(data):
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cursor = conn.cursor()

    _SQL = "insert into reddit (header, image, news_link, all_text,comments) values (%s,%s,%s,%s,%s)"

    cursor.execute(_SQL, (data['header'],
                          data['image'],
                          data['news_link'],
                          data['all_text'],
                          data['comments']))

    conn.commit()
    cursor.close()
    conn.close()


def drop_sql():
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cur = conn.cursor()
    try:
        cur.execute("drop table reddit")
    except Exception:
        print()

    conn.commit()
    cur.close()
    conn.close()


def create_sql():
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE Reddit
        (
        HEADER TEXT NOT NULL,
        IMAGE TEXT NOT NULL,
        NEWS_LINK TEXT NOT NULL,
        ALL_TEXT TEXT NOT NULL,
        COMMENTS TEXT NOT NULL
        )

        """)

    conn.commit()
    cursor.close()
    conn.close()


urls = []
driver = webdriver.Firefox()
driver.get('https://www.reddit.com/search/?q=план маршала')
news = driver.find_elements_by_xpath("//a[@class='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE']")
all_text = []
comments = []
drop_sql()
create_sql()
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
    write_pstgres(data)
