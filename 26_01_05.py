# 2. 리스트 선언과 접근
# 01. 빈 리스트 선언
members = []
print(members)
# 02. 값이 있는 리스트 선언
members = ["가나다", "라마바", "사아자"]
print(members)
# 03. 리스트 첫 번째 요소 접근
members = ["가나다", "라마바", "사아자"]
first = members[0]
print(first)
# 04. 리스트 마지막 요소 접근
members = ["가나다", "라마바", "사아자"]
last = members[-1]
print(last)
# 05. 리스트 길이 확인
members = ["가나다", "라마바", "사아자"]
count = len(members)
print(count)
# 06. 리스트에 요소 추가(append)
members = ["가나다"]
members.append("라마바")
print(members)
# 07. 리스트 특정 위치 요소 수정
members = ["가나다", "라마바", "사아자"]
members[1] = "추가 요소"
print(members)
# 08. 리스트 요소 삭제(pop)
members = ["가나다", "라마바", "사아자"]
removed = members.pop(1)
print(removed)
print(members)