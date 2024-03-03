def parse_value(text):
    parts = text.split('=', 1)
    return (parts[0].strip(), parts[1].strip())


print(parse_value('url=http://www.python.org'))