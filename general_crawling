API_Key = 'AIzaSyDCOWFI1LbAMLu5FjW0dveJSXkN8-fUDd8'

import os
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from django.utils import timezone
from mini_url.models import Article
import requests



def website(site,cseid):
    CustSearchEngID = cseid
    query = site
    r = requests.get(
        'https://www.googleapis.com/customsearch/v1?key=' + API_Key + '&cx=' + CustSearchEngID + '&q=' + query + '&dateRestrict=d4')
    print(r.json())
    return(r.json())


def links(data):
    links = []
    for line in data:
        if line == 'items':
            for i in range(len(data['items'])):
                links += [data['items'][i]['link']]
    return (links)


def info(data):
    for links in data:
        try:
            Article.objects.get(url=links)
            print(links + " already exists")
        except Exception as E:
            params = (('url', links),)
            r2 = requests.get('https://labs.diffbot.com/testdrive/analyze', params=params)
            data2 = r2.json()
            print(data2)
            for line in data2:
                if line == 'objects':
                    try:
                        Article.objects.get(name=data2['objects'][0]['title'])
                        print(data2['objects'][0]['title'] + " already exists")
                    except Exception as E1:
                        Article.objects.create(name=data2['objects'][0]['title'],
                                               url=data2['objects'][0]['pageUrl'], date=datetime.strptime(data2['objects'][0]['date'][5:22], "%d %b %Y %H:%M"),
                                               text=data2['objects'][0]['text'], website = data2['objects'][0]['siteName'])


def run():
    websites = [('www.retailgazette.co.uk','005030095173212139980:xkjj9e5fcme'), ('https://www.ii.co.uk','005030095173212139980:nwjv_irb8ko'),('https://www.retail-week.com','005030095173212139980:7bwqozdytsw')]
    for (site,cseid) in websites:
        data = website(site,cseid)
        link = links(data)
        info(link)


if __name__ == '__main__':
    run()
