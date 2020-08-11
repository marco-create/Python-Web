'''
Import and print topic chosen by the user from Wikipedia
Libraries:
- wikipedia
- wikipediaapi

creation -- MN 11.08.2020
edited   -- 
'''

import wikipediaapi, wikipedia
wiki_main = wikipediaapi.Wikipedia('en')

## select main topic
main_topic = input('Choose a topic (wikipedia): ')

try:
    print('\nDisambiguation:')
    for e,t in enumerate(wikipedia.search(main_topic)):
        print(e,t)
    choice = int(input('Choose topic by index: \n'))

    w = wikipedia.search(main_topic)[choice]    ## use search to the chosen topic
    print(w)

    page = wiki_main.page(w)
    sections = []
    for s in page.sections:
        sections.append(s.title)

    ## enumerate the sections of the chosen page. Decide which one to print or all
    for n,s in enumerate(sections):
        print(n,s)
    section_idx = input('\nChoose a section (by its index) or type [all] to see: ').lower()
    if section_idx == 'all':
        print(page.text)
    else:
        print(f'\n{page.section_by_title(sections[int(section_idx)])}')
except:
    ## exit if missing page
    page_missing = wiki_main.page('The page you typed does not exist.')
    print(f'Page - Exists: {page_missing.exists()}')
