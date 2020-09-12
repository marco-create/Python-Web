import time
import webbrowser
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


def youtube_topic(yt_search):

	print('============\nYOUTUBE\n============')
	
	PATH = "C:\Program Files (x86)\chromedriver.exe"	## chrome executable on Windows
	options_chrome = Options()
	options_chrome.add_argument('headless')   ## no UI  
	#yt_search = input('What are you looking for in YouTube? ')
from GoogleNews import GoogleNews
gnews = GoogleNews(lang='en')
run = True

print('============\nGOOGLE NEWS\n============')
main_topic = input('Choose a topic: ')

while run:
    try:
        gnews.search(main_topic)
        for n, result in enumerate(gnews.result()):
            print(n, result['title'])

        ## choose which article to pick
        article = input('\nChoose an article by its main index or choose [all] to visualize all links: ')
        if article == 'all':
            [print(f'{n}: {new}') for n, new in enumerate(gnews.gettext())]
            [print(f'{n}: {link}') for n, link in enumerate(gnews.get__links())]
        else:
            article = int(article)
            print(f'Article - Title: {gnews.gettext()[article]}')
            list_artcl = gnews.gettext()
            print(f'Article - Link: {gnews.get__links()[article]}')
            list_links = gnews.get__links()
        print('==========================================================================\n')
        go_further = input('DO you want to read other articles? (y/n) ').lower()
        if go_further == 'y' or go_further == 'yes':
            gnews.clear()   ## before going in loop, needs to clears the article list
        else:
            run = False ## break the loop

    except:
        print('Error :S')
        run = False ## break the loop
