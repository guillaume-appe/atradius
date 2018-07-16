# import requests
#
# url = 'https://gateway-fra.watsonplatform.net/knowledge-studio/tools/app/rzhz10/tbm0p7g8e91l14x1/ui/#/'
#
# login_data = dict(username='pjw', password='', csrfmiddlewaretoken=csrf, next='/')
# r = requests.post(URL, data=login_data, headers=dict(Referer=url))
#
# print(r.content)

import requests
url1 = 'https://idaas.iam.ibm.com/idaas/mtfim/sps/authsvc?PolicyId=urn:ibm:security:authentication:asf:basicldapuser/authsvc/mtfim/sps/authsvc?StateId=16c9c6c7-c427-4e65-8767-20f458aea979'
values = {'username': 'peter@verticaldataanalytics.com',
          'password': 'Haarlem123!'}

r = requests.post(url1, data=values)
print(r.url)



# /authsvc/mtfim/sps/authsvc?StateId=16c9c6c7-c427-4e65-8767-20f458aea979
#
# https://idaas.iam.ibm.com/idaas/mtfim/sps/authsvc?PolicyId=urn:ibm:security:authentication:asf:basicldapuser