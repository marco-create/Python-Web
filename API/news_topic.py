from GoogleNews import GoogleNews

main_topic = input('Choose a topic: ')

gnews = GoogleNews(lang='en')
try:
    gnews.search(main_topic)
    for n, result in enumerate(gnews.result()):
        print(n, result['title'])

    ## choose which article to pick
    article = int(input('\nChoose an article by its main index: '))
    print('Article - Title: ', gnews.gettext()[article])
    list_artcl = gnews.gettext()
    print('Article - Link: ', gnews.get__links()[article])
    list_links = gnews.get__links()
    print('==========================================================================')
    

except:
    print('Error :S')