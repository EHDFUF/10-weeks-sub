import math

a = 2020 #a라는 식별자이자 변수에 2020 저장

b = 3030 #b라는 식별자이자 변수에 3030 저장

a += b 

print(a)

#파이썬에서 제공해주는 수 형태 : 정수실수복소수 

#파이썬에서 제공하는 사칙연산 : +(덧셈) -(뺄셈) *(곱셈) **(제곱) /(나누기) //(나머지버림나눗셈) %(나머지도출연산)

print(3/2)
print(3//2)
print(5%2)

print(hex(6))

print(hex(888))


print(hex(888))

print(bin(888))

print(oct(888))

# 부동소수는 소수점 15자리까지 제공

# 수를 다룹시다 abs() : 절대값 의미 , 제공받은 수의 절대값을 반환 / round() 해당 수의 반올림 반환 / trune 버림계산

print(abs(-3))

print(round(1.6))

print(math.trunc(1.7)) # 아 trunc은 mathe 모듈 내에서 제공하는 함수라 앞에 math.를 붙어야함

# 팩토리얼은 영어 해석 상 factorial() 함수 그대로 씀

print(math.factorial(6))

# 제곱연산 ** 은 math모듈에서 제공하는 pow()와 같음 반대로 제곱근은 sqrt()로 계산

print(3**3)
print(math.pow(3,4))

print(math.sqrt(9))

print(math.log(81, 3))

print(math.log(math.e))

print(math.log10(100000))

# 다시한번강조 : input()의 결과물은 예외없이 다 문자열 : 숫자로 사용하고 싶으먄 int(input())을 해야함함


a = 333 

b = bin(a)

print(a<<3)


print(True & False)

a = 6 # 0110

print(a<<1) # 0110 의 비트를 왼쪽으로 한칸씩 이동(이떄 공백은 0으로 채우기) # 1100 = 12

# &(and) |(or) Xor(~OR) ~(Not)

# 숫자에 대한 논리곱 연산은 1. 일단 각 숫자들을 2진수로 변환 2. 각 자릿수에 대해 논리곱 연산을 한다 3. 결과물을 출력한다

print(9 and 10) # 9 = 1001 , 10 = 1010 이러면 9 and 10 은 아마도 8이 나와야함함

# 제발 기억할 포인트 : 숫자에 대한 논리연산은 각각의 비트에 대한 계산 후 각각을 더한 값을 출력하는 것임

print(9 ^ 10) 

# 보수 (0,1 뒤집기) 는 Not으로 수행

print(~12)

print(f"{100 + 100}")

print("%d" %(100 + 100))

print("%d + %d" %(100, 200))

print("{2:d} {0:d} {1:d}".format(100,200,300)) # format 문자 앞 숫자는 해당 format에 들어있는 인덱스의 순서를 나타낸 것 
