import requests

cookies = {
    'WKS-XSRF-TOKEN': 'tPSvw2zjEkkFsT/lfOQpATHcRJTbB2lmUohpQhlYMTlTC7pK8nzoqJwABTTJE+4e2xrZFG1v50ankJVTqSBR87wGW+rcZlhKikM8tD96jyhjavdjxkrGmQb77HJOxZ2q',
    'Watson-DPAT': 'P7g7EJsmg0JVPNt3G5JgTE2ejcC3L73GCxBX7GMVmny8VxU03JWR9yalHAQk7ndMhjkp4KG20%2BHxVu9LVoNiKbH8%2BaTqOFVLO3vax9H4rwSfgRhzx7D7nRS%2BYXVt65d2pzCv34RlOvvQpuPewNcYux6n%2BBAGnP2er%2FuMwBaMfNpEst%2BooB15dSJce4s2cD5ql8AHnN5Wj4niVd00cruTlPggF5xAYdfjSvkPpNrPV%2BF1qUhlHq8RjqdKmhje4yYC9LUE1Xm0inH%2BNp7Rt65HIYDN5pnL8VEzvBpg02Z%2F843O1bwcmsU8zOYhiq8e%2BHNpNAqzo907vt%2F67SkbYAmvF5%2BIUiyGPFY6ipKLN%2BS%2B8P17hI3r0V8l9vKuh1TmBbQ99XlcJixHNAenSYbrAdGCTvCmRI5%2FwrLwj8TYhCJMyIifsVR92W0RDApZiJyXMnx72Z6kXjn9s8NgKD7GU75n%2FvbILN8FUdURPsqvHZHpG%2BdhQWFDGySCcITUxe5Aw1OYA32WS8ntkAU8Jsp5e9nS7GDdh%2Fj7%2BDv34u6bkYKGnVlNNq2xEVaG4RnktfoKt%2BYc8DWHdQqiZMFRZ8LusLWOGkM0aSX9relJBaWYUhIbEKF22i79zVxF2oUpiLcDS1REXjw9dhyXLMGP9rjbMGMezUWUV9fsCIyttc4Z86JTsq25%2FrVXpMmchenAmRwCYtxDpDP2IU3In078kw%2FVbWcx3NM%2FexRJ5KOxQyrRBPCr5HCxX13L9imyiyOBwMLhkWB3RqEogi04l8ZJj9I9YOKyAQ4syCG80shjLW%2F7D3kXUeQaZHrmPwe5N1V8e%2FlviqAU8j5ARyueOtk9p7%2FIkqURStAnHQBlPsgz24r8zFwhhnG1zl0rstFRHmMGnhYuxcaMkVy2%2F0E9RLoCJG57jNqZn6lpd4zwAnpI4jUU%2Brh8VG%2F8MPpFRtgNJwBdOlLGmOyQ%2BqAALhZJICfRpObxA%2FC%2BqMXqjQGtCBIlT7R5pt13UoyHpZQGscQ%2BrUQ%2B0eMAcf0e79qYY3C1JVi%2BYuoq482ee1p8tiEcXVZhqe5wuOmXTPBEdW8NnxdCabMFYd1yVj9G3F%2BOQYzGB%2FcCXhdnXQY1DfovmnrVoQjR6YeULGGkn1JiqnwoLyIhAd6rn8K2ux%2FD90XCgzpQABKRmXLLxzAKeAh9XaygpwLcYImYjURJOujwH6AXrhJtD1RbRlx5VVkwKwVlrDFTWwlW6RIdVACKWyGWTXitfZGvjZPHuKIE7MzYLLqFgI1Jaxw4CsROT6P1k%2BNTpwE8gg3W5O1gLcuqKk9P0HP6eW3UXKsYRUK3%2B5TzG%2BGK%2FoURtdms2tFN0DKAjUncT7ibMlrgG3vb5iAIPVCfFME88mqRlOi39pRgjV2Np6G6VNHqBEc5IWLfsBrOJYyoGiv%2Bsjq1MxIgSc9I9hYQLuVbd4akq21%2BCBblCGkl5LHyJ54zfyLww63NGxbfSnApCuh24cf0%2B9s6aVQ77%2FQUcB6VnlqsNBVbAD%2BG9c46ddfOpTcZu8hpALYq5ZiKUcYqLspc4V%2F8nO5uUUH6mBeyQ1nEDVBdhRrkkcs5IG4aCG%2FaymI94V2q76CEI3CUCyfyqZP5eIe%2BIepoN7z%2BgnrawTF5RHYfZMCoT5cCz5xj0N1HBkggLa7kaq2VAobw2JDo73lafDZBQnqGsxsTs9bHR%2FEmtlL90Yvqfn34I%2BLk92rUknqBg8b2FPFjvonKE6bdrXkuaOce0FqkUpun28OerQDea0QPTJe93UIzyiGk9oQzgQ79xlhPtnIMCTWyrivrxKpHbCP0nVNHvLbpi8bdB6%2F4zr8rKOhXbPKI%2F7X3rXNsFZuM1MvY4%2BJ%2BtHMN%2FKA3n9k779Azx1zYRs5%2FTiZQnkq4k5nzDomaZD20nFjMaI2l1cJ2FTmoMdmTc2JokNwelpqoysrj2U6e08qJ4P3Pu8CHNtjbba2pKPquRGTckxXkpt2IqzHXUpp8viVorJI5bIaqL8Y4avH7ldDM7J0HSBdS9ZKdS41dyEaRzPnYfuXhSywcdx6EBPA5RG6PzU4FGXmIHzA%2BZrnuysBztzxLNEwZYs3dPaWz8Ig8kogym3td5GImw0OpANsnrojRX652eF5ezdu4Ucni0ZEjmJw6Sm9mU%2FXViiBJJIooUsLtEmUIZ3xb5tNLmzppxY8RpTxSltrXC6eCr1sHH94gyGZ8Ai9CqRka62RvPEx7Cf9ko7OZtXoF9LEy5N3DR9Wk45Djz0bCD4eEMnG%2Fo9WwsOYelCIbSy9YCcclKLdNe1R0m5taTmh5SN56Ub6hHxl7ZwJ1C8OiY7QggdMniR8KR63FmaKRBo%2BE9GCKXsbCfvmqmuLu2Ms4P3HggCh1Rfkmn%2BQ0O5ObBKgGaX%2BO5t9dWd21rOWhI%2FJBqgjm%2FwSWAKWUEgryFGmJ1xmAQ1XVfmuIeBWxA0PnM%2BZvksVLMgdlKWTlCZM4hXjW4o4DcVL974UtlXi%2FZMJG1M%2Fuwm0uBskJo8K5exl%2FN5eik7Q1kF4B6Wty6ButBz2xTl1yjB9AxJI1%2FKaQ1w0n9ASzRv9LtNxDGAytDaFUOsd%2B887cU7ualSWXMNlqBvwdomBc2OFY86qk398M6TtKdjkuQVIcTTVEapXRLaWoZsqDgNwpmxD4MFJv%2FoaOORlIItPvOYnDN9lY%2BFK7VVAzcOXqp5EJWVDtbZlUlJoAaytGPhAnVRufQ%2BGtA10Azsu7%2BZ%2BzztYXqPHDzHYOEbJUjGcH9uCQZB8rtdR8bXJul6mx0cFJBuiULOKZ7wm5zJ%2BzTLSyug%2F%2BujM5qrd7yt2SMM20S7R0JuO%2FJYfccVDnrBYPjl33BqAtrFUnpfD5NPWCcyrwTcy144QkhSBmQ8qqm0uiwPEICgFq8Mceuo6Ih78fveUDnfVFZP9ypNuAxuXL6I%2FWWAHLDM6SESK8JrQHit7HBb7b2sOl9pJDzisDW4X%2FWkaTg9RUj67D0F3Azm7Fzc54smsKC7hqoNEzVA8%2FNPTLj5fFhZuApXKA%2BdEVquI4uS2fNfI30eFXrhLzQNK0DKDhXMQo3iEInDLzRQ9ZuQJo0noI%2B50wb8q5b1fdQ2PwU5PEkukD6w%3D%3D',
}

headers = {
    'x-wks-xsrf-token': 'tPSvw2zjEkkFsT/lfOQpATHcRJTbB2lmUohpQhlYMTlTC7pK8nzoqJwABTTJE+4e2xrZFG1v50ankJVTqSBR87wGW+rcZlhKikM8tD96jyhjavdjxkrGmQb77HJOxZ2q',
}

response = requests.get('https://gateway-fra.watsonplatform.net/knowledge-studio/tools/app/rzhz10/tbm0p7g8e91l14x1/wks/api/v10/workspaces/6adbab40-8045-11e8-918a-1d9f128137ac/rules/class', headers=headers, cookies=cookies)

data = response.json()

for line in data:
    a= line.get('name')
    cookies = {
        'WKS-XSRF-TOKEN': 'tPSvw2zjEkkFsT/lfOQpATHcRJTbB2lmUohpQhlYMTlTC7pK8nzoqJwABTTJE+4e2xrZFG1v50ankJVTqSBR87wGW+rcZlhKikM8tD96jyhjavdjxkrGmQb77HJOxZ2q',
        'InitialxWatsonURI': '/knowledge-studio/tools/app/rzhz10/tbm0p7g8e91l14x1/ui/',
        'Watson-DPAT': 'P7g7EJsmg0JVPNt3G5JgTE2ejcC3L73GCxBX7GMVmny8VxU03JWR9yalHAQk7ndMhjkp4KG20%2BHxVu9LVoNiKbH8%2BaTqOFVLO3vax9H4rwSfgRhzx7D7nRS%2BYXVt65d2pzCv34RlOvvQpuPewNcYux6n%2BBAGnP2er%2FuMwBaMfNpEst%2BooB15dSJce4s2cD5ql8AHnN5Wj4niVd00cruTlPggF5xAYdfjSvkPpNrPV%2BF1qUhlHq8RjqdKmhje4yYC9LUE1Xm0inH%2BNp7Rt65HIYDN5pnL8VEzvBpg02Z%2F843O1bwcmsU8zOYhiq8e%2BHNpNAqzo907vt%2F67SkbYAmvF5%2BIUiyGPFY6ipKLN%2BS%2B8P17hI3r0V8l9vKuh1TmBbQ99XlcJixHNAenSYbrAdGCTvCmRI5%2FwrLwj8TYhCJMyIifsVR92W0RDApZiJyXMnx72Z6kXjn9s8NgKD7GU75n%2FvbILN8FUdURPsqvHZHpG%2BdhQWFDGySCcITUxe5Aw1OYA32WS8ntkAU8Jsp5e9nS7GDdh%2Fj7%2BDv34u6bkYKGnVlNNq2xEVaG4RnktfoKt%2BYc8DWHdQqiZMFRZ8LusLWOGkM0aSX9relJBaWYUhIbEKF22i79zVxF2oUpiLcDS1REXjw9dhyXLMGP9rjbMGMezUWUV9fsCIyttc4Z86JTsq25%2FrVXpMmchenAmRwCYtxDpDP2IU3In078kw%2FVbWcx3NM%2FexRJ5KOxQyrRBPCr5HCxX13L9imyiyOBwMLhkWB3RqEogi04l8ZJj9I9YOKyAQ4syCG80shjLW%2F7D3kXUeQaZHrmPwe5N1V8e%2FlviqAU8j5ARyueOtk9p7%2FIkqURStAnHQBlPsgz24r8zFwhhnG1zl0rstFRHmMGnhYuxcaMkVy2%2F0E9RLoCJG57jNqZn6lpd4zwAnpI4jUU%2Brh8VG%2F8MPpFRtgNJwBdOlLGmOyQ%2BqAALhZJICfRpObxA%2FC%2BqMXqjQGtCBIlT7R5pt13UoyHpZQGscQ%2BrUQ%2B0eMAcf0e79qYY3C1JVi%2BYuoq482ee1p8tiEcXVZhqe5wuOmXTPBEdW8NnxdCabMFYd1yVj9G3F%2BOQYzGB%2FcCXhdnXQY1DfovmnrVoQjR6YeULGGkn1JiqnwoLyIhAd6rn8K2ux%2FD90XCgzpQABKRmXLLxzAKeAh9XaygpwLcYImYjURJOujwH6AXrhJtD1RbRlx5VVkwKwVlrDFTWwlW6RIdVACKWyGWTXitfZGvjZPHuKIE7MzYLLqFgI1Jaxw4CsROT6P1k%2BNTpwE8gg3W5O1gLcuqKk9P0HP6eW3UXKsYRUK3%2B5TzG%2BGK%2FoURtdms2tFN0DKAjUncT7ibMlrgG3vb5iAIPVCfFME88mqRlOi39pRgjV2Np6G6VNHqBEc5IWLfsBrOJYyoGiv%2Bsjq1MxIgSc9I9hYQLuVbd4akq21%2BCBblCGkl5LHyJ54zfyLww63NGxbfSnApCuh24cf0%2B9s6aVQ77%2FQUcB6VnlqsNBVbAD%2BG9c46ddfOpTcZu8hpALYq5ZiKUcYqLspc4V%2F8nO5uUUH6mBeyQ1nEDVBdhRrkkcs5IG4aCG%2FaymI94V2q76CEI3CUCyfyqZP5eIe%2BIepoN7z%2BgnrawTF5RHYfZMCoT5cCz5xj0N1HBkggLa7kaq2VAobw2JDo73lafDZBQnqGsxsTs9bHR%2FEmtlL90Yvqfn34I%2BLk92rUknqBg8b2FPFjvonKE6bdrXkuaOce0FqkUpun28OerQDea0QPTJe93UIzyiGk9oQzgQ79xlhPtnIMCTWyrivrxKpHbCP0nVNHvLbpi8bdB6%2F4zr8rKOhXbPKI%2F7X3rXNsFZuM1MvY4%2BJ%2BtHMN%2FKA3n9k779Azx1zYRs5%2FTiZQnkq4k5nzDomaZD20nFjMaI2l1cJ2FTmoMdmTc2JokNwelpqoysrj2U6e08qJ4P3Pu8CHNtjbba2pKPquRGTckxXkpt2IqzHXUpp8viVorJI5bIaqL8Y4avH7ldDM7J0HSBdS9ZKdS41dyEaRzPnYfuXhSywcdx6EBPA5RG6PzU4FGXmIHzA%2BZrnuysBztzxLNEwZYs3dPaWz8Ig8kogym3td5GImw0OpANsnrojRX652eF5ezdu4Ucni0ZEjmJw6Sm9mU%2FXViiBJJIooUsLtEmUIZ3xb5tNLmzppxY8RpTxSltrXC6eCr1sHH94gyGZ8Ai9CqRka62RvPEx7Cf9ko7OZtXoF9LEy5N3DR9Wk45Djz0bCD4eEMnG%2Fo9WwsOYelCIbSy9YCcclKLdNe1R0m5taTmh5SN56Ub6hHxl7ZwJ1C8OiY7QggdMniR8KR63FmaKRBo%2BE9GCKXsbCfvmqmuLu2Ms4P3HggCh1Rfkmn%2BQ0O5ObBKgGaX%2BO5t9dWd21rOWhI%2FJBqgjm%2FwSWAKWUEgryFGmJ1xmAQ1XVfmuIeBWxA0PnM%2BZvksVLMgdlKWTlCZM4hXjW4o4DcVL974UtlXi%2FZMJG1M%2Fuwm0uBskJo8K5exl%2FN5eik7Q1kF4B6Wty6ButBz2xTl1yjB9AxJI1%2FKaQ1w0n9ASzRv9LtNxDGAytDaFUOsd%2B887cU7ualSWXMNlqBvwdomBc2OFY86qk398M6TtKdjkuQVIcTTVEapXRLaWoZsqDgNwpmxD4MFJv%2FoaOORlIItPvOYnDN9lY%2BFK7VVAzcOXqp5EJWVDtbZlUlJoAaytGPhAnVRufQ%2BGtA10Azsu7%2BZ%2BzztYXqPHDzHYOEbJUjGcH9uCQZB8rtdR8bXJul6mx0cFJBuiULOKZ7wm5zJ%2BzTLSyug%2F%2BujM5qrd7yt2SMM20S7R0JuO%2FJYfccVDnrBYPjl33BqAtrFUnpfD5NPWCcyrwTcy144QkhSBmQ8qqm0uiwPEICgFq8Mceuo6Ih78fveUDnfVFZP9ypNuAxuXL6I%2FWWAHLDM6SESK8JrQHit7HBb7b2sOl9pJDzisDW4X%2FWkaTg9RUj67D0F3Azm7Fzc54smsKC7hqoNEzVA8%2FNPTLj5fFhZuApXKA%2BdEVquI4uS2fNfI30eFXrhLzQNK0DKDhXMQo3iEInDLzRQ9ZuQJo0noI%2B50wb8q5b1fdQ2PwU5PEkukD6w%3D%3D',
        'cmapi_gtm_bl': '',
        'notice_gdpr_prefs': '0|1|2:',
        'cmapi_cookie_privacy': 'permit_1|2|3',
        'BMAID': '329ee31b-d9de-4a0a-b019-726ac5bfba69',
        'CoreID6': '22012234029715314847253&ci=51860000|PRODUCTUSAGE_50200000|CLOUDEXCHANGE',
        'CoreM_State': '88~-1~-1~-1~-1~3~3~5~3~3~7~7~|~~|~~|~~|~||||||~|~~|~~|~~|~~|~~|~~|~~|~',
        'CoreM_State_Content': '6~|~~|~|',
        'utag_main': 'v_id:0164939a5d8700173faf3d58f88702079005b0710093c$_sn:1$_ss:0$_st:1531486537524$ses_id:1531484724616%3Bexp-session$_pn:2%3Bexp-session$is_country_member_of_eu:true$mm_sync:1%3Bexp-session$dc_visit:1$dc_event:2%3Bexp-session$dc_region:eu-central-1%3Bexp-session',
        'OPTOUTMULTI': '0:0%7Cc1:1%7Cc2:0%7Cc3:0',
        'notice_behavior': 'expressed|eu',
        'notice_preferences': '2:',
        'ajs_user_id': '%22IBMid-50HY84BC4V%22',
        'ajs_group_id': 'null',
        'ajs_anonymous_id': '%22329ee31b-d9de-4a0a-b019-726ac5bfba69%22',
        'LtpaToken2': 'K92pqnRiemwGJjoSltZX0C2+nYnShGKMpHg0bcvmoTrNsE3evT30DYjcIYmtmVBWicoe4L9e2aWCGz5xcN/VqD2/TX5lAlVQ5wHQ2ROe7X1HlgK//fc5oCZ9F612mYuNuSbUZ60oCOp/ra/fPAq2mPm0yQkIvolHX3Op1iP5cxjpnfvZCrhmIsepjSAw1gSCUg5GmtGi80u/cTtY63346D0apcXouAdOZihTpQhZdoWplG/BnquZdOa6Fmv+yWXaXzShNUqxjqP02jEL84WQDpzu6XqMCEzFnfO2/vNDPsnYsNqZ/AFGwshA02L5EhmrAM3G2H5Mc2L6BYMeAWbaIgW2QFqwpN61UnGYnR1logXWaWAistdBLWqinSF9NeSx14u0bnLJDORtNWOn5lPTBg==',
        'intercom-session-ydoy8e4i': 'NjgydDZ2cXRxb2hGVDVzQzN3TTA5QkZ0ZlJLL3hjQ1Q4QVlFeTR1aUFKcnVjOThHOU1xbWx2SnptNlpLengvUC0tWDhGRFpXQVZUdFpYWWVjTDdmQys3dz09--87adb1060f92473b102b0be70929060dd067562a',
        'intercom-lou-ydoy8e4i': '1',
    }

    headers = {
        'Host': 'gateway-fra.watsonplatform.net',
        'accept': 'application/json, text/plain, */*',
        'origin': 'https://gateway-fra.watsonplatform.net',
        'x-wks-xsrf-token': 'tPSvw2zjEkkFsT/lfOQpATHcRJTbB2lmUohpQhlYMTlTC7pK8nzoqJwABTTJE+4e2xrZFG1v50ankJVTqSBR87wGW+rcZlhKikM8tD96jyhjavdjxkrGmQb77HJOxZ2q',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'referer': 'https://gateway-fra.watsonplatform.net/knowledge-studio/tools/app/rzhz10/tbm0p7g8e91l14x1/ui/',
        'accept-language': 'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
    }

    params = (
        ('create_default_role', 'true'),
    )

    data2 = '{"label":'+'"'+ a +'"' + ',"properties":{},"sireProp":{"roles":[]}}'
    response = requests.post('https://gateway-fra.watsonplatform.net/knowledge-studio/tools/app/rzhz10/tbm0p7g8e91l14x1/wks/api/v10/workspaces/6adbab40-8045-11e8-918a-1d9f128137ac/typestore/entitytypes', headers=headers, params=params, cookies=cookies, data=data2)
