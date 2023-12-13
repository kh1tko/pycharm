from typing import List, Union


def to_int(a_list: List[str]) -> List[int]:
    return [int(e) for e in a_list]


def calc(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


if __name__ == '__main__':
    print(to_int(['2', '1', '9']))
print(calc(8, 7))
