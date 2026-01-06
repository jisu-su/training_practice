# 2. 딕셔너리를 담은 리스트
# 2-1. 딕셔너리 하나를 리스트에 추가
members = []
person = {"name": "가나다", "age": 26}
members.append(person)
print(members)
# 2-2. 딕셔너리 여러 개를 리스트로 구성
members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27},
    {"name": "사아자", "age": 28}
]
print(members)
# 2-3. 리스트 내 첫 번째 딕셔너리 접근
members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27}
]
first = members[0]
print(first)
# 2-4. 리스트 내 딕셔너리의 특정 키 값 접근
members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27}
]
name = members[0]["name"]
print(name)
# 2-5. for문으로 딕셔너리 리스트 전체 순회
members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27},
    {"name": "사아자", "age": 28}
]
for member in members:
    print(member)
# 2-6. 순회하며 특정 키 값만 출력
members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27},
    {"name": "사아자", "age": 28}
]
for member in members:
    print(member["name"])
# 2-7. 순회하며 특정 조건 딕셔너리만 출력
members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27},
    {"name": "사아자", "age": 28}
]
for member in members:
    if member["age"] >= 27:
        print(member)
# 2-8. 순회하며 딕셔너리 내 값 수정
members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27}
]
for member in members:
    member["age"] = member["age"] + 1
print(members)