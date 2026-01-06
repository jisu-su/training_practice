# 4. Create, Read Update 조합
# 4-1. 이름과 나이 입력 받아 딕셔너리로 리스트에 추가
name = input()
age = int(input())

members = []
person = {"name": name, "age": age}
members.append(person)

print(members)
# 4-2. 전체 목록 순회하며 이름만 출력
members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27},
    {"name": "사아자", "age": 28}
]

for member in members:
    print(member["name"])
# 특정 이름 검색하여 해당 딕셔너리 출력
keyword = input()

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27},
    {"name": "사아자", "age": 28}
]

for member in members:
    if member["name"] == keyword:
        print(member)
# 4-4. 특정 이름의 나이 수정
target_name = input()
new_age = int(input())

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27}
]
for member in members:
    if member["name"] == target_name:
        member["age"] = new_age

print(members)
# 4-5. 인덱스로 접근하여 값 수정
idx = int(input())
new_name = input()

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27}
]
members[idx]["name"] = new_name

print(members)
# 4-6. 조건에 맞는 항목만 필터링하여 출력
min_age = int(input())

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27},
    {"name": "사아자", "age": 28}
]
filtered = []
for member in members:
    if member["age"] >= min_age:
        filtered.append(member)

print(filtered)
# 4-7. 메뉴 선택에 따라 다른 동작 수행
menu = input()

members = [
    {"name": "가나다", "age": 26},
    {"name": "사아자", "age": 27}
]

if menu == "1":
    print(members)
elif menu == "2":
    print(len(members))
else:
    print("잘못된 입력")
# 4-8. 반복 입력과 조회를 while로 구성
members = []
while True:
    cmd = input()
    if cmd == "q":
        break
    name = input()
    age = int(input())
    members.append({"name": name, "age":age})

print(members)