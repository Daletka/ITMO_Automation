def ta(a = (1, 2, 3, 4)):
    return a[0]

print(ta((5, 6, 7, 8)))

def pl(radius, pi=3.14159):
    return pi*(radius**2)
print(pl(2))

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print(indent('123',10))