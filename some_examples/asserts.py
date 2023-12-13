# Написать функцию проверки надежности пароляб возращает всегда строку
# - если пароль короче 8 символов то вернуть Too weak
# - если содержит только цифрі, только строчніе, только заглавніе то вернуть Weak
# - если пароль содержит символы любых двух наборов то вернуть Good
# - если пароль содержит символы любых 3 наборов, вернуть Very Good
import string


def password_strength(value: str) -> str:
    if len(value) < 8:
        return 'Too weak'
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count += 1
            continue
    if count == 3:
        return 'Very Good'
    return 'Weak' if count == 1 else 'Good'


if __name__ == '__main__':
    assert password_strength('') == 'Too weak'
    assert password_strength('1234567') == 'Too weak'
    assert password_strength('qwerty') == 'Too weak'
    assert password_strength('QWERTY') == 'Too weak'
    assert password_strength('QWErty1') == 'Too weak'
    assert password_strength('12345678') == 'Weak'
    assert password_strength('12345678987654321') == 'Weak'
    assert password_strength('qwertyui') == 'Weak'
    assert password_strength('QWERTYUI') == 'Weak'
    assert password_strength('QWERTYASDFGH') == 'Weak'
    assert password_strength('1234qazw') == 'Good'
    assert password_strength('1234QWER') == 'Good'
    assert password_strength('qwerQWER') == 'Good'
    assert password_strength('AERQWE14as') == 'Very Good'
