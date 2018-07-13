import requests

url = 'https://gateway-fra.watsonplatform.net/knowledge-studio/tools/app/rzhz10/tbm0p7g8e91l14x1/ui/'

login_data = dict(username='pjw', password='', csrfmiddlewaretoken=csrf, next='/')
r = requests.post(URL, data=login_data, headers=dict(Referer=url))

print(r.content)


# Check if it worked?
#print
#r.status_code