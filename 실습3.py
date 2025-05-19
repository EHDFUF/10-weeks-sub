select, answer, num_str, num1, num2 = 0,0,'',0,0

select = int(input("1, 2 중 하나만 입력해바")) # 1, 2에 따라 결과가 달라짐짐

if select == 1: # 1이면
    num_str = input("수식입력해보셈")
    answer = eval(num_str)
    print(f"{num_str}의 결과는 {answer}임")


elif select == 2:
    num1 = int(input("첫번째숫자입력"))
    num2 = int(input("두번째숫자입력"))
    for number_count in range(num1, num2 + 1):
        answer += number_count

    print(f"{num1}+...+{num2}의 결과물이 {answer}이다")

else:
    print("1or2중에만타이핑하삼")
