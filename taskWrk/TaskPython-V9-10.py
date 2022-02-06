# typing

# Модуль typing содержит дополнительные типы для аннотаций

from typing import Optional, Union, Callable, Sequence, Generator, Iterable, Iterator

def f1(a: int) -> int:
    return a*2

print(f1(5))

def f2(a: Union[int, float]) -> Union[int, float]:
    return a*2

print(f2(5))

print(f"Результат: {Optional[int] == Union[int, None]}")

def doubler(value: str, callback: str = None) -> str:
        """rerurn rezult string"""
        if callback == 'Y':
            cal_number = '+375'+value
            return cal_number
        else:
            return f"not callback"

print(doubler('291234567', 'Y'))


# End