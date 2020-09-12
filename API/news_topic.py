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
            print('--')
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
