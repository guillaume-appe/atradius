from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version = '2018-03-19',
    username = 'c8f96476-896a-427f-b4a4-818058b814f2',
    password = 'OULSSEKSZOwG',
    url = 'https://gateway-fra.watsonplatform.net/natural-language-understanding/api',
)

response = natural_language_understanding.analyze(
    text = 'Independent Auditor’s Report INDEPENDENT AUDITOR’S REPORT TO THE SHAREHOLDERS OF MOTORSPORTSTORE UK LTD We have audited the financial statements of Motorsportstore UK Ltd for the year ended 31 December 2016, set out on pages 6 to 15. The relevant financial reporting framework that has been applied in their preparation is applicable law and the United Kingdom Accounting Standards (United Kingdom Generally Accepted Accounting Practice), including Financial Reporting Standard 102 The Financial Reporting Standard applicable in the UK and Republic of Ireland. This report is made solely to the Companys members, as a body, in accordance with Chapter 3 of Part 16 of the Companies Act 2006. Our audit work has been undertaken so that we might state to the Company‘s members those matters we are required to state to them in an Auditors report and for no other purpose. To the fullest extent permitted by law, we do not accept or assume responsibility to anyone other than the Company and the Companys members as a body, for our audit work, for this report. or for the opinions we have formed. Respective responsibilities of Directors and Auditor As explained more fully in the Directors responsibilities statement on, the directors are responsible for the preparation of the financial statements and for being satisfied that they give a true and fair view. Our responsibility is to audit and express an opinion on the financial statements in accordance with applicable law and International Standards on Auditing (UK and Ireland). Those standards require us to comply with the Financial Reporting Councils Ethical Standards for Auditors. Scope of the audit of the financial statements An audit involves obtaining evidence about the amounts and disclosures in the financial statements sufficient to give reasonable assurance that the financial statements are free from material misstatement, whether caused by fraud or error. This includes an assessment of whether the accounting policies are appropriate to the Companys circumstances and have been consistently applied and adequately disclosed; the reasonableness of significant accounting estimates made by the directors; and the overall presentation of the financial statements. In addition, we read all the financial and non-financial information in the Directors report to identify material inconsistencies with the audited financial statements and to identify any information that is apparently materially incorrect based on, or materially inconsistent with, the knowledge acquired by us in the course of performing the audit. If we become aware of any apparent material misstatements or inconsistencies we consider the implications for our report. Qualified opinion on financial statements Except for the possible effects of the matter described in the Basis for Qualified Opinion paragraph, in our opinion the financial statements: a give a true and fair view of the state of the Companys affairs as at 31 December 2016 and of its loss for the year then ended; 0 have been properly prepared in accordance with United Kingdom Generally Accepted Accounting Practice; and a have been prepared in accordance with the requirements of the Companies Act 2006. Basis for qualified opinion on financial statements With respect of stock having a carrying amount of £44,202 at 31 December2015 the audit evidence available to us was limited because we did not observe the counting of the physical stock on that date, since that date was prior to our appointment as auditor of the company. Owing to the nature of the companys records, we were unable to obtain sufficient appropriate audit evidence regarding the stock quantities by using other audit procedures. Emphasis of matter These financial statements have been prepared on the break up basis as the directors do not consider that the going concern basis of preparation is appropriate. Further details are given in the Directors Report and in note 1. Opening balances The financial statements for the prior period were not audited.',
    features = Features(entities=EntitiesOptions(model='20:e9836516-b9be-4856-a894-d0bf6a75aeb8')),
    return_analyzed_text = True,
)

a = json.dumps(response, indent=2)
#print(a)
b = json.loads(a)
#print(b)

c = b['analyzed_text']
#print(c)

