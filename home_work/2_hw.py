# Задача 1
def task_1(a: int = 2, b: float = 3.5, c: str = "python", d=None, e: bool = True) -> None:
    if d is None:
        d = [1, 2, 3]
    return print('\n', a, " относится к типу ", type(a), '\n', b, " относится к типу ", type(b), '\n',
                 c, " относится к типу ", type(c), '\n', d, " относится к типу ", type(d), '\n',
                 e, " относится к типу ", type(e), '\n', )

task_1()

# Задача 2
def task_2(a=None) -> list:
    if a is None:
        a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]

print("Первые три числа последовательности Фибоначчи: ", task_2())


# Задача 3
def task_3(a: int) -> int:
    return a ** 2

print(task_3(5))
