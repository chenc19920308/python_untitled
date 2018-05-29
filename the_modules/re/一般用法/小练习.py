import re
p = re.compile(r'\d{3}-\d{6}')
print(p.findall('010 -628888'))

# re.search(r"(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5]\.)","192.168.1.1")