# 1. 딕셔너리 선언과 접근
# 1-1. 빈 딕셔너리 선언
person = {}
print(person)
# 1-2. 키-값 쌍이 있는 딕셔너리 선언
person = {"name": "가나다", "age": 26}
print(person)
# 1-3. 딕셔너리에서 특정 키로 값 접근
person = {"name": "가나다", "age": 26}
name = person["name"]
print(name)
# 1-4. 딕셔너리에 새 키-값 추가
person = {"name": "가나다"}
person["age"] = 26
print(person)
# 1-5. 딕셔너리 특정 키의 값 수정
person = {"name":"가나다", "nickname": "라마바"}
person["nickname"] = "사아자"
print(person)
# 1-6. 딕셔너리 키 존재 여부 확인
person = {"name": "가나다", "age": 26}
result = "name" in person
print(result)
# 1-7. 딕셔너리 키-값 삭제
person = {"name": "가나다", "age": 26, "nickname": "라마바"}
del person ["nickname"]
print(person)
# 1-8. 딕셔너리 전체 키 목록 확인
person = {"name": "가나다", "age": 26}
keys = list(person.keys())
print(keys)