"""
Some temporary scripts
"""
from pprint import pprint as pp
from person.get_quotes import get_quotes
from person.extract import extract_persons
from person.get_quotes import _encode_quotes_in_quotes

text = """
მრჩეველი, მიხაილო პოდოლიაკი
              """


resp = extract_persons(text)
print(resp)
