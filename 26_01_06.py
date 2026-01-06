# 3. 조건문 기초
# 3-1. if문 단독 사용
name = "가나다"
if name == "가나다":
    print(name)
# 3-2. if-else 사용
age = 26
if age >= 30:
    print("30대")
else:
    print("20대")
# 3-3. if-elif-else 사용
age = 26
if age < 20:
    print("10대")
elif age < 30:
    print("20대")
else:
    print("30대 이상")
# 3-4. 숫자 비교 조건문
age = int(input())
result = ""
if age > 26:
    result = "가나다보다 많음"
elif age == 26:
    result = "가나다랑 동갑"
else:
    result = "가나다보다 적음"
print(result)
# 3-5. 문자열 비교 조건문
nickname = input()
result = ""
if nickname == "라마바":
    result = "마바입니다"
elif nickname == "사아자":
    result = "아자입니다"
else:
    result = "알 수 없음"
print(result)
# 3-6. in 연산자로 포함 여부 확인
keyword = input()
members = ["가나다", "라마바", "사아자"]
if keyword in members:
    print("존재함")
else:
    print("존재하지 않음")
#  3-7. and 조건 사용
name = "가나다"
age = 26
if name == "가나다" and age == 26:
    print("본인 확인 완료")
else:
    print("본인 아님")
# 3-8. or 조건 사용
nickname = "사아자"
if nickname == "라마바" or nickname == "사아자":
    print("별명 있음")
else:
    print("별명 없음")
