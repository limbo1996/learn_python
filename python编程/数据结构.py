if n >= 0:
    param = 0
else:
    param = -n
result = foo(param)

param = n if n >= 0 else -n

result = foo(n if n >= 0 else -n)

