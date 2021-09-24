from itertools import cycle
import re


def extract_login_password(text):
    login = re.findall(r'Login: (.*)', text)[0]
    password = re.findall(r'Password: (.*)', text)[0]

    return login, password


def extract_ips(text):
    ip_port_pattern = (
        r'((?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}'
        r'(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])'
        r':\d{2,5})'
    )

    return re.findall(ip_port_pattern, text)


def get_proxy_generator():
    with open('proxies.txt', 'r') as file:
        text = file.read()

    ip_addresses = extract_ips(text)
    login, password = extract_login_password(text)

    proxies = []

    for ip_address in ip_addresses:
        proxy = {'http': f'http://{login}{password}@{ip_address}'}
        proxies.append(proxy)

    return cycle(proxies)
