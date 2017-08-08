import re
strIntegers = "1 2 3  mark 4 5"
def fnIntMatchTo(objMatch):
    print(objMatch.group('num') + ".0")

pattern = r"(?P<num>[0-9]+)"
regexp = re.compile(pattern)
regexp.sub(fnIntMatchTo, strIntegers)
