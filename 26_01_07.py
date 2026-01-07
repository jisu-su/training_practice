# 1. 함수 정의 기초
# 1-1. 매개 변수 없는 함수 정의와 호출
def greet():
    print("안녕하세요")

greet()
# 1-2. 매개변수 하나 있는 함수
def greet(name):
    print(name)

greet("가나다")
# 1-3. 매개변수 두 개 있는 함수
def introduce(name, age):
    print(name, age)

introduce("가나다", 26)
# 1-4. 반환값 없는 함수
def show_name(name):
    print(name)

result = show_name("가나다")

print(result)
# 1-5. 반환값 있는 함수
def get_name():
    return "가나다"

result = get_name()

print(result)
# 1-6. 리스트를 매개변수로 받는 함수
def show_all(members):
    for member in members:
        print(member)

data = ["가나다", "라마바", "사아자"]
show_all(data)
# 1-7. 딕셔너리를 매개변수로 받는 함수
def show_person(person):
    print(person["name"], person["age"])

data = {"name": "가나다", "age": 26}
show_person(data)