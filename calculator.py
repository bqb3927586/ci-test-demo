def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# 故意写语法错误：缺少闭合括号
result = add(10, 20
print(f"Result: {result}")
