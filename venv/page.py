from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

path = '/Users/guillaumeappe/Desktop/'
filename = 'Auditors.docx'
txt= getText(path+filename)


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version = '2018-03-19',
    username = 'c8f96476-896a-427f-b4a4-818058b814f2',
    password = 'OULSSEKSZOwG',
    url = 'https://gateway-fra.watsonplatform.net/natural-language-understanding/api',
)

response = natural_language_understanding.analyze(
    text = txt,
    features = Features(entities=EntitiesOptions(model='20:e9836516-b9be-4856-a894-d0bf6a75aeb8')),
    return_analyzed_text = True,
)

a = json.dumps(response, indent=2)
b = json.loads(a)

res = []
for type in b['entities']:
    a = type['text']
    res += [(a,txt.find(a))]
    list = sorted(res, key = lambda place: place[1])


def annotate(text,list):
    doc = docx.Document()
    a = 0
    para = 0
    for tuple in list:
        phrase = tuple[0]
        d = len(phrase)
        e = text.find(phrase)
        doc.add_paragraph(text[a:(e-1)])
        para+=1
        doc.add_paragraph(text[e:(d + e)])
        doc.paragraphs[para]='underline'
        para+=1
        a = d + e + 1
    doc.add_paragraph(text[a:len(text)])
    doc.save(path+'annotate_'+filename)

annotate(txt,list)