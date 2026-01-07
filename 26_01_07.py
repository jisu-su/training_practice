# 2. CRUD 함수화 
# # 2-1. 데이터 추가 함수 (Create) - 이름만
# name = input()

# members = []

# def add_member(members, name):
#     members.append(name)

# add_member(members, name)
# print(members)
# # 2-2. 데이터 추가 함수 (Create) - 이름과 나이
# name = input()
# age = int(input())

# members =[]

# def add_member(members, name, age):
#     person = {"name": name, "age": age}
#     members.append(person)

# add_member(members, name, age)
# print(members)
# # 2-3. 전체 조회 함수 (Read) - 리스트 출력
# members = [
#     {"name": "가나다", "age": 26},
#     {"name": "라마다", "age": 27}
# ]

# def read_all(members):
#     for member in members:
#         print(member)

# read_all(members)
# # 2-4. 전체 조회 함수 (Read) - 번호와 함께 출력
# members = [
#     {"name": "가나다", "age": 26},
#     {"name": "라마다", "age": 27}
# ]

# def read_all_with_index(members):
#     for idx, member in enumerate(members):
#         print(idx, member["name"], member["age"])

# read_all_with_index(members)
# # 2-5. 단건 조회 함수 (Read) - 인덱스로 검색
# idx = int(input())

# members = [
#     {"name": "가나다", "age": 26},
#     {"name": "라마바", "age": 27}
# ]

# def read_by_index(members, idx):
#     return members[idx]

# result = read_by_index(members, idx)
# print(result)
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