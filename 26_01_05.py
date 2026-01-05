# 3. for문 기초
# 01. 리스트 전체 순회 출력
members = ["가나다", "라마바", "사아자"]
for member in members:
    print(member)
# 02. range로 숫자 순회
numbers = range(3)
for num in numbers:
    print(num)
# 03. enumerate로 인덱스와 함께 순회
members = ["가나다", "라마바", "사아자"]
for idx, member in enumerate(members):
    print(idx, member)
# 04. 순회하며 특정 조건 요소만 출력
members = ["가나다", "라마바", "사아자"]
for member in members:
    if member == "라마바":
        print(member)
# 05. 순회하며 새 리스트에 추가
members = ["가나다", "라마바", "사아자"]
new_list = []
for member in members:
    new_list.append(member)
print(new_list)
# 06. 순회하며 값 누적
ages = [26, 27, 28]
total = 0
for age in ages:
    total = total + age
print(total)