# 2. CRUD 함수화 
# 2-1. 데이터 추가 함수 (Create) - 이름만
name = input()

members = []

def add_member(members, name):
    members.append(name)

add_member(members, name)
print(members)
# 2-2. 데이터 추가 함수 (Create) - 이름과 나이
name = input()
age = int(input())

members =[]

def add_member(members, name, age):
    person = {"name": name, "age": age}
    members.append(person)

add_member(members, name, age)
print(members)
# 2-3. 전체 조회 함수 (Read) - 리스트 출력
members = [
    {"name": "가나다", "age": 26},
    {"name": "라마다", "age": 27}
]

def read_all(members):
    for member in members:
        print(member)

read_all(members)
# 2-4. 전체 조회 함수 (Read) - 번호와 함께 출력
members = [
    {"name": "가나다", "age": 26},
    {"name": "라마다", "age": 27}
]

def read_all_with_index(members):
    for idx, member in enumerate(members):
        print(idx, member["name"], member["age"])

read_all_with_index(members)
# 2-5. 단건 조회 함수 (Read) - 인덱스로 검색
idx = int(input())

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27}
]

def read_by_index(members, idx):
    return members[idx]

result = read_by_index(members, idx)
print(result)
# 2-6. 단건 조회 함수 (Read) - 이름으로 검색
keyword = input()

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27}
]

def read_by_name(members, keyword):
    for member in members:
        if member["name"] == keyword:
            return member
    return None

result = read_by_name(members, keyword)
print(result)
# 2-7. 수정 함수(Update) - 인덱스와 새 값 받기
idx = int(input())
new_age = int(input())

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27}
]

def update_by_index(members, idx, new_age):
    members[idx]["age"] = new_age

update_by_index(members, idx, new_age)
print(members)
# 2-8. 수정 함수(Update) - 이름으로 찾아 수정
target_name = input()
new_age = int(input())

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27}
]

def update_by_name(members, target_name, new_age):
    for member in members:
        if member["name"] == target_name:
            member["age"] = new_age

update_by_name(members, target_name, new_age)
print(members)
# 2-9. 삭제 함수 (Delete) - 인덱스로 삭제
idx = int(input())

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27},
    {"name": "사아자", "age": 28}
]

def delete_by_index(members, idx):
    members.pop(idx)

delete_by_index(members, idx)
print(members)
# 2-10. 삭제 함수 (Delete) - 이름으로 찾아 삭제
target_name = input()

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27},
    {"name": "사아자", "age": 28}
]

def delete_by_name(members, target_name):
    for i, member in enumerate(members):
        if member["name"] == target_name:
            members.pop(i)
            break

delete_by_name(members, target_name)
print(members)
# 2-11. 검색 함수 - 조건에 맞는 항목 반환
min_age = int(input())

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27},
    {"name": "사아자", "age": 28}
]

def search_by_age(members, min_age):
    result = []
    for member in members:
        if member["age"] >= min_age:
            result.append(member)
    return result

filtered = search_by_age(members, min_age)
print(filtered)
# 2-12. 개수 반환 함수
members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27}
]

def get_count(members):
    return len(members)

count = get_count(members)
print(count)
