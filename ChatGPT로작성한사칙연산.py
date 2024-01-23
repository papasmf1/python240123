def add(x, y):
    """두 수를 더하는 함수"""
    return x + y

def subtract(x, y):
    """두 수를 빼는 함수"""
    return x - y

def multiply(x, y):
    """두 수를 곱하는 함수"""
    return x * y

def divide(x, y):
    """두 수를 나누는 함수"""
    if y != 0:
        return x / y
    else:
        return "나누는 수(y)는 0이 될 수 없습니다."

# 예제 사용
num1 = 10
num2 = 5

#f-string: format string python 3.6 
print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")
