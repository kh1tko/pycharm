def usdcny(usd):
    cny = usd * 6.25
    new_cny = '{:.2f}'.format(cny)
    return f'{new_cny} Chinese Yuan'


def hello(name=None):
    if name is None:
        return f'Hello, World!'
    elif 0 < len(name):
        return f'Hello, {name.capitalize()}!'
    else:
        return f'Hello, World!'


print(hello(None))
