import requests
# import nltk
# nltk.download('gutenberg')

response = requests.get('https://www.asx.com.au/asx/statistics/todayAnns.do')

a=response.content
txt = a.decode("utf-8")
#print(txt)

#b=txt.find('href="/asx/statistics/displayAnnouncement.do?display')
b = txt.find('Quarterly Activities Report')
print(b)


# url = 'https://www.asx.com.au/asxpdf/20170929/pdf/43msrfn10c82y7.pdf'
# r = requests.get(url, stream=True)
#
# with open('/Users/guillaumeappe/Desktop/doc.pdf', 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=1024):
#         fd.write(chunk)
