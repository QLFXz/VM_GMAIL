import requests
import re
import urllib.parse
from urllib.parse import urlparse, parse_qs
email=input("Email=")
if "@gmail.com" not in email:
        print("Invalid email address")
        print("Please enter a valid email address with Gmail Domain")
        exit(1)
email.split('@')
US=email.split('@')
US=US[0]
url = 'https://accounts.google.com/servicelogin?hl=en-gb'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'accounts.google.com',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"121.0.6167.161"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.161", "Chromium";v="121.0.6167.161"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Chrome-ID-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=8f1f3932-1eb5-4090-9f2b-252e0ea14109,signin_mode=all_accounts,signout_mode=show_confirmation',
    'X-Client-Data': 'CI+VywE='
}

# Send initial GET request
response = requests.get(url, headers=headers)
response_url = response.url

# Parse necessary parameters from the response URL
parsed_url = urlparse(response_url)
query_params = parse_qs(parsed_url.query)
ifkv = query_params.get('ifkv', [None])[0]
dsh = query_params.get('dsh', [None])[0]

# Quote ifkv and dsh for use in subsequent URLs
ifkv = urllib.parse.quote(ifkv)
dsh = urllib.parse.quote(dsh)

# Construct URL for signup flow with parsed parameters
signup_url = f'https://accounts.google.com/lifecycle/flows/signup?biz=false&dsh={dsh}&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en-gb&ifkv={ifkv}&theme=glif'

# Prepare headers for the signup flow
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'accounts.google.com',
    'Referer': 'https://accounts.google.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Chrome-ID-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=8f1f3932-1eb5-4090-9f2b-252e0ea14109,signin_mode=all_accounts,signout_mode=show_confirmation',
    'X-Client-Data': 'CI+VywE=',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"121.0.6167.161"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.161", "Chromium";v="121.0.6167.161"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0'
}

# Create a session to manage cookies
session = requests.Session()

# Send request to signup URL
response = session.get(signup_url, headers=headers)

# Extract TL parameter from the response URL
response_url = response.url
parsed_url = urlparse(response_url)
query_params = parse_qs(parsed_url.query)
TL = query_params.get('TL', [None])[0]

# Quote TL for use in the final payload URL
TL = urllib.parse.quote(TL)

# Use regex patterns to extract AT and FdrFJe values from response text
snlmoe_pattern = r'"SNlM0e":"([^"]+)"'
fdrfje_pattern = r'"FdrFJe":"([^"]+)"'
snlmoe_match = re.search(snlmoe_pattern, response.text)
fdrfje_match = re.search(fdrfje_pattern, response.text)
AT = urllib.parse.quote(snlmoe_match.group(1)) if snlmoe_match else None
FdrFJe = urllib.parse.quote(fdrfje_match.group(1)) if fdrfje_match else None

post_url = f'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute?rpcids=E815hb&source-path=%2Flifecycle%2Fsteps%2Fsignup%2Fname&f.sid={FdrFJe}&bl=boq_identity-account-creation-evolution-ui_20240208.02_p2&hl=en-gb&TL={TL}&_reqid=407217&rt=c'

payload = f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22Harold%5C%22%2C%5C%22%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C1%2C1%5D%2Cnull%2C%5B%5D%2C%5B%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={AT}&'
LEN = len(payload)

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': f'{LEN}',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Host': 'accounts.google.com',
    'Origin': 'https://accounts.google.com',
    'Referer': 'https://accounts.google.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Chrome-ID-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=8f1f3932-1eb5-4090-9f2b-252e0ea14109,signin_mode=all_accounts,signout_mode=show_confirmation',
    'X-Client-Data': 'CI+VywE=',
    'X-Same-Domain': '1',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"121.0.6167.161"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.161", "Chromium";v="121.0.6167.161"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
    'x-goog-ext-391502476-jspb': f'["{dsh}",null,null,"{ifkv}"]'
}

response = session.post(post_url, data=payload, headers=headers)

url=(f'https://accounts.google.com/lifecycle/steps/signup/birthdaygender?TL={TL}&dsh={dsh}&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en-gb&ifkv={ifkv}&theme=glif')
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'accounts.google.com',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121","Chromium";v="121"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"121.0.6167.161"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.161","Chromium";v="121.0.6167.161"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Chrome-ID-Consistency-Request': 'version=1,client_id',
    'X-Client-Data': 'CI+VywE='
}

response = session.get(url, headers=headers)
fdrfje_match = re.search(fdrfje_pattern, response.text)
FdrFJe = urllib.parse.quote(fdrfje_match.group(1)) if fdrfje_match else None
url=f'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute?rpcids=eOY7Bb&source-path=%2Flifecycle%2Fsteps%2Fsignup%2Fbirthdaygender&f.sid={FdrFJe}&bl=boq_identity-account-creation-evolution-ui_20240208.02_p2&hl=en-gb&TL={TL}&_reqid=309055&rt=c'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Host': 'accounts.google.com',
    'Origin': 'https://accounts.google.com',
    'Referer': 'https://accounts.google.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Chrome-ID-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=8f1f3932-1eb5-4090-9f2b-252e0ea14109,signin_mode=all_accounts,signout_mode=show_confirmation',
    'X-Client-Data': 'CI+VywE=',
    'X-Same-Domain': '1',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"121.0.6167.161"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.161", "Chromium";v="121.0.6167.161"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
    'x-goog-ext-391502476-jspb': f'["{dsh}",null,null,"{ifkv}"]'
}
payload=f'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B1999%2C1%2C1%5D%2C1%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C1%2C1%5D%2C%5C%22%3CxQlqCVECAAajugZng7qNVnUOPnQYop30ADQBEArZ1B6j7w8Uv8giVqAgzuPVvIA2XDCvV1SmYCWASaCIaN8PL7ZcE3buFHd0Wa7wGtoCzQAAAKedAAAAA6cBB1YHryeM4mO77iPiuTzu3P7tMbdL8aOoP6hx_5pRchqJXEBIm1fCOBQfj_wWypx7HDCrvrWxkOc7t3z-kH2Z72p7gsozI2LTfe1E9yNNzBONDH6f6rYu-F0Bx1Yl6_yQqzSgswF0Bpq3dBdFRrlS20nAYxFWzW0-U_QX2YfZGwJbDbCqWGqgaaYIj6q8n3ojD6_DcuUVjimPpmEkcfJZXoLpl2VK7gDfkmRyBglNiZiFyAxof1Dzoc_f2gqhh6l-WD8x1RuVHEouAIg6gV2ngSLnKGaW5PY7Vzv8Bu7LVmxkb6QE_YpmdKGSIktksXwMm7HK09bQtzBtyxZ5aBExgh-7gSq894cn7-G3dnb7Zkym-QezMR2EDyCYmufBzKqSzKEYDPr9uK_dMpd7Cd6kXjxls7Z5tMv6DzzTfU1mdvfEbANJ_kTU-U180q2HMpwDxlEcO__xZh5KUyqA_c0qdh8-hAScHpiCFs4tikJTh5fHK4TcafiwNsl0sp31yRZbHKzufmONTy9hrGLIf_6NAJnpy5EXSZ0aa2igt2j3pIomKxrU6p9Z1ZooW_1sEHEUvdTR2ZNz8PMCOj95FJyUhhPVt_SSOlg0wramlRA7puZxPKoQ0fYDZU-_cs24b5RZn6a8KwOJwbaaPgoSHebaiu9mYwQoh_F67HRO1-BNZkk1aybHgFnMUjdiaxvphByJL-HahGLQ9ej5Ha_Ub89Swc6i-igN87Z195_xew3x7bzPc7FLIpeIX_46yRXKjd6ETC73AafieKrmQWgF0nc__oiTZvbtv3vIrBQ914-7TXRvBu1N6OX5athmRCVMq8TeFNo5n1npkUm642DaXBCouMPtehBbmDekebggN5wA9GC-sfTHUfTQXQrCEY8zgC3-0W8qGOU98dfnkpVykHsUbvcXaNj9wJJ5quzKS-W39V6-7EoV_Ve2qpBNvoeE8AHH7tTVbLOiIpwRCdIJdwfNxD494r-m1JEBR_HifaHqfh011fksqQeF4pM40PresxUnarYD40lrg76fRA_uAuNU-kQFfk4kehq37YWhY60S0uwdzBraauoKEGT5HMNeOGzGrS9aNrcLLlKetpvSAO3ype-7Gje-vZq7_CZ57p63pIOkh43fmjvNYbsMwGEyBXZaYXWyAHPEX8qERe5IcilFP0wlWJtXBot0ig-w35qUn_fLbrv38HjQtyAsnu9wUpPpBN3OUaUgUXoSR--BVs6fdDzMdLygFGmiH8gDUQfti2ObSbQEtS5oHe-gB00qQ2CFjxSHNFhTB1naRxq1W_wSAPnGpxub9dWGzuEZ0_lBWkYDomx9vaeDUUS3EXXAgL4WfdI49BLPCVwm5NkiaHRZ-iq9OxjfhOSDWDiC3jq9NqFMzUnjMfJzjq-tkQcpr3HeCxCx_kJdFr99P_s49u9aJRPKEAqFedmJuNW6ul0sj7gfglu2DiCU2o71A_fgb5AZ1pD0JuI5DdZ-KE3phiCVVBZV-u3Wjj1FKFJJSRMrSMff-c5vXy14lgq4wGdIPtjqGZFcFyRes8F0FDn2AyNIcpD4LpKKg3wU5W0tE2vWA4RRUskli96ccd7SK35x6lauduMLPHxONhpTkvEQ45lucAaAv0va80vtrtD55g9HAj0iTxKwj5TL7DFfJ-0WS-w1gliuZ6IPfd5267pdbkjrRpnIXi4eqmUKMab_Hlf9_ZukC3f1cIUpjer4SW8fMpK3wlZtqUNoFZPavILmAenAkY59Ejx4TnBKQGwUhTW_78JR5OTOgKeE6rMQ28YodODdjhLDbOsMP1NTJ3KAzN0VTKh0QKmGxi1EzrW64vGsKzYdCiVbGrVf_ru8eTa3_GlbFByuSgZe3r8SU6N3MG2NCeadgW5rqjkiJLXIk9aPB0uS2sVrRHWqvm1JnTxmLPSZk7lUpMteJ-RtgxCotAqnTfiDVqKD1ApIRCUIRo0kpatT_tLb5UM_Li8a-IVnn_peH2srAq1mDo6tLthA1T2Ypz-57FQPVD6PXL-BCj7CQX0mS4n75j6v7BhIxlrmLOydGV3gh7VKfEQkgqL_vXdSuHRF6bzSCGAgI7moFcmDFXt2QCWEqaZx33Nl50CJq0EdUwylxdia2m_64BqWXMmCQe6BIQj1c8dVMArmF9YAl8M8J9L1XbSOTGCncNBaoKk9q9kWqYKV8Yn-cX8qndjXOF5Ws3IjWry7Xza4gMj-7CaYf-ioVP37ZZrtI7YOrrgsJVM1OvHkF7sAx3y_GL3HoqqFAVP-pa0_Nxse20s6v1ghr7RGzzN2O_tBccNGr24gPaVHqILBKYm36icKP2OZ1fn-Tsaexk-eM768P4bdEOd08w_Vo8EkYg0GUkr82rEHg50_T1OZRznUnKgakKorx_IaJgMknKDRzxB8EzjciW8zd_sHRjttT7VchbsZqgPnDnJNF0D_iSjvPxJ3d8ZqXtDNPPwVNweL_Ah0APZS1O0fuXD_HfemzqiBZErHbgbGDXTkeFkxL-pQjFIrHlknW5phQ1D7pxKHFyTchdjaVHo0SPGpDNbyf-6cP92oSFSfJLEYnd-EkBiV7QyBVT5VlLwNxPHHXzObxNMM2d89T6OHLtxMd60RKBHzHb-fzcnc_WTS%5C%22%2C%5B%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={AT}&'
response=session.post(url,data=payload,headers=headers)
url=f'https://accounts.google.com/lifecycle/steps/signup/username?TL={TL}&dsh={dsh}&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en-gb&ifkv={ifkv}&theme=glif'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'accounts.google.com',
    'Referer': 'https://accounts.google.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Chrome-ID-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=8f1f3932-1eb5-4090-9f2b-252e0ea14109,signin_mode=all_accounts,signout_mode=show_confirmation',
    'X-Client-Data': 'CI+VywE=',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"121.0.6167.161"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.161", "Chromium";v="121.0.6167.161"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0'
}
response = session.get(url, headers=headers)
fdrfje_match = re.search(fdrfje_pattern, response.text)
FdrFJe = urllib.parse.quote(fdrfje_match.group(1)) if fdrfje_match else None
url=f'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute?rpcids=NHJMOd&source-path=%2Flifecycle%2Fsteps%2Fsignup%2Fusername&f.sid={FdrFJe}&bl=boq_identity-account-creation-evolution-ui_20240208.02_p2&hl=en-gb&TL={TL}&_reqid=209557&rt=c'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Host': 'accounts.google.com',
    'Origin': 'https://accounts.google.com',
    'Referer': 'https://accounts.google.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Chrome-ID-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=8f1f3932-1eb5-4090-9f2b-252e0ea14109,signin_mode=all_accounts,signout_mode=show_confirmation',
    'X-Client-Data': 'CI+VywE=',
    'X-Same-Domain': '1',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"121.0.6167.161"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.161", "Chromium";v="121.0.6167.161"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
    'x-goog-ext-391502476-jspb': f'["{dsh}",null,null,"{ifkv}"]'
}
payload=f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{US}%5C%22%2C1%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C151712%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={AT}&'
response = session.post(url, data=payload, headers=headers)

if response.status_code == 200:
    if 'steps/signup/password' in response.text:
        print('AVILABLE EMAIL TO CREATE')
    elif 'Sorry, your username must be' in response.text:
        print("Sorry, your username must be between 6 and 30 characters long.")
    else:
        print("!!EXIST EMAIL!!")
else:
    print(f'Request failed with status code: {response.status_code}')


