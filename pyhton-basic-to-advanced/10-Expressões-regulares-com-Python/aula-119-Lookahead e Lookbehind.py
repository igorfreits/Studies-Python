"""Lookahead e Lookbehind"""
import re
from pprint import pprint

texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''
# Positive Lookahead(Palavra apos o padrão) - ?=
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))
pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Negative Lookahead - ?!
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))


# Positive Lookbehind(Palavra antes do padrão) - ?<=
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
pprint(re.findall(r'\w+(?<=OFFLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Negative Lookbehind - ?<!
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
pprint(re.findall(r'\w+(?<!OFFLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

