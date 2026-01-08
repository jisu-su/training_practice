# 3. 함수 조합과 흐름 제어
# 3-1. 메뉴 출력 함수
def show_menu():
    print("1. 추가")
    print("2. 조회")
    print("3. 종료")

show_menu()
# 3-2. 입력 처리 함수
def get_person_input():
    name = input()
    age = int(input())
    return {"name": name, "age": age}

person = get_person_input()
print(person)
# 3-3. 메뉴 선택에 따라 함수 호출 분기
menu = input()

members = [
    {"name": "가나다", "age": 26}
]

def read_all(members):
    for member in members:
        print(member)

def get_count(members):
    return len(members)

if menu == "1":
    read_all(members)
elif menu == "2":
    print(get_count(members))
# 3-4. while과 함수 조합으로 반복 메뉴
def show_menu():
    print("1. 조회")
    print("2. 종료")

def read_all(members):
    for member in members:
        print(member)

members = [
    {"name": "가나다", "age": 27}
]

while True:
    show_menu()
    menu = input()
    if menu == "1":
        read_all(members)
    elif menu == "2":
        break
# 3-5. 함수 내에서 다른 함수 호출
def get_name():
    return "가나다"

def get_greeting():
    name = get_name()
    return name + "님 안녕하세요"

message = get_greeting()
print(message)
# 3-6. 함수 반환값을 다른 함수의 인자로 전달
def create_person(name,age):
    return {"name": name, "age": age}

def show_person(person):
    print(person["name"], person["age"])

person = create_person("가나다", 26)
show_person(person)
# 3-7. 유효성 검사 함수
idx = int(input())

members = [
    {"name": "가나다", "age": 26},
    {"name": "라마바", "age": 27}
]

def is_valid_index(members, idx):
    if idx >= 0 and idx < len(members):
        return True
    return False

if is_valid_index(members, idx):
    print(members[idx])
else:
    print("잘못된 인덱스")
# 3-8. 전체 흐름을 main 함수로 묶기
def show_menu():
    print("1. 조회")
    print("2. 종료")

def read__all(members):
    for member in members:
        print(member)

def main():
    members = [
        {"name": "가나다", "age": 26}
    ]
    while True:
        show_menu()
        menu = input()
        if menu == "1":
            read__all(members)
        elif menu == "2":
            break

main()
# 3-9. CRUD 전체를 함수 기반으로 구성 
def show_menu():
    print("1. 추가")
    print("2. 전체조회")
    print("3. 수정")
    print("4. 삭제")
    print("5. 종료")

def add_member(members):
    name = input()
    age = int(input())
    members.append({"name": name, "age": age})

def read_all(members):
    for idx, member in enumerate(members):
        print(idx, member["name"], member["age"])

def update_member(members):
    idx = int(input())
    new_age = int(input())
    members[idx]["age"] = new_age

def delete_member(members):
    idx = int(input())
    members.pop(idx)

def main():
    members = []
    while True:
        show_menu()
        menu = input()
        if menu == "1":
            add_member(members)
        elif menu == "2":
            read_all(members)
        elif menu == "3":
            update_member(members)
        elif menu == "4":
            delete_member(members)
        elif menu == "5":
            break

main()