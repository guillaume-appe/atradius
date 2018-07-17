import requests

cookies = {
    'cmapi_gtm_bl': '',
    'BMAID': '329ee31b-d9de-4a0a-b019-726ac5bfba69',
    'notice_gdpr_prefs': '0|1|2:',
    'cmapi_cookie_privacy': 'permit_1|2|3',
    'CoreM_State': '0~-1~-1~-1~-1~3~3~5~3~3~7~7~|~~|~~|~~|~||||||~|~~|~~|~~|~~|~~|~~|~~|~',
    'CoreM_State_Content': '6~|~8BFABB42E13D8981~E80B3D19A8B6EC5D~|~0~1',
    'CoreID6': '88036867554715312983407&ci=50200000|Bluemix_52640000|Bluemix_50200000|IBM_GlobalMarketing_52640000|IBM_GlobalMarketing_50200000|IBM_Watson_52640000|IBM_Watson_50200000|MYIBM_50200000|ECOM_52640000|ECOM_50200000|SLAwebsite',
    'ajs_group_id': 'null',
    'ajs_user_id': '%22IBMid-50HY84BC4V%22',
    'ajs_anonymous_id': '%22329ee31b-d9de-4a0a-b019-726ac5bfba69%22',
    'UnicaNIODID': 'PkBYGG7isg1-a78IfkX',
    'DPJSESSIONID-DAL-P': 'PBC5YS:1668517345',
    'PD_STATEFUL_9fe53814-694b-11e6-8919-005056a467f6': '%2Fidaas',
    'PD_STATEFUL_0f5b6fd2-0839-11e8-a21b-005056a467f6': '%2Fauthsvc',
    'IBMID_USER': 'ldap%7Cpeter%40verticaldataanalytics.com',
    'PD-S-SESSION-ID': '1_2_0_cJu--8T--tXyNMPsZMOTM9M0kQEf8ysfC8gG6nTWbnPUl3cM',
    'notice_behavior': 'expressed|eu',
    'notice_preferences': '2:',
    'cvo_sid1': 'E27FWZ7MMWMY',
    'optimizelyEndUserId': 'oeu1531482442741r0.3978996164911768',
    '_uetsid': '_uet85c7171d',
    'utag_main': 'v_id:0164887e5c22000f2f814f8290fd02079001a0710093c$_sn:8$_ss:0$_st:1531835195406$is_country_member_of_eu:true$dc_visit:7$ses_id:1531833392799%3Bexp-session$_pn:2%3Bexp-session$mm_sync:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:eu-west-1%3Bexp-session',
    'OPTOUTMULTI': '0:0%7Cc1:1%7Cc2:0%7Cc3:0',
    'cvo_tid1': 'BDu9hNqFvsA|1531298345|1531833395|0',
    '50200000_clogin': 'l=33352161531833394401&v=1&e=1531835196755',
    '52640000_clogin': 'l=45073931531833394408&v=1&e=1531835196757',
    'idaasRedirectUrl': 'https://idaas.iam.ibm.com/idaas/oidc/endpoint/default/authorize?client_id=ZTdhOWU4MmQtOTA1MC00&scope=openid&state=9d5b171d-e78b-454d-8b0c-0978113821e1&nonce=6e261d9f-aea5-40ab-9081-e048a916a6b9&response_type=code&redirect_uri=https%3A//iam.eu-de.bluemix.net/oidc/callback/IBMid',
}

headers = {
    'Host': 'idaas.iam.ibm.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://idaas.iam.ibm.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
    'Content-Type': 'application/json',
    'Referer': 'https://idaas.iam.ibm.com/idaas/mtfim/sps/authsvc?PolicyId=urn:ibm:security:authentication:asf:basicldapuser',
    'Accept-Language': 'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
}

data = '{"user":"peter@verticaldataanalytics.com","oidcUrl":true}'

response = requests.post('https://idaas.iam.ibm.com/v1/mgmt/idaas/user/identitysources', headers=headers, cookies=cookies, data=data)

print(response.url)


#https://idaas.iam.ibm.com/idaas/mtfim/sps/authsvc?PolicyId=urn:ibm:security:authentication:asf:basicldapuser