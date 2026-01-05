# 4. Create와 Read 조합
# 01. 이름 하나 입력 받아 리스트에 추가 후 전체 출력
name = input()
members = []
members.append(name)
print(members)
# 02. 이름 세 개 입력 받아 리스트에 추가 후 전체 출력
name1 = input()
name2 = input()
name3 = input()
members = []
members.append(name1)
members.append(name2)
members.append(name3)
print(members)
# 03. 이름 입력 받아 추가, 전체 개수 출력
name = input()
members = ["가나다", "라마바"]
members.append(name)
count = len(members)
print(count)
# 04. 반복문으로 여러 이름 입력 받아 리스트 구성
members = []
for i in range(3):
    name = input()
    members.append(name)
print(members)
# 05. 리스트에서 특정 이름 검색
keyword = input()
members = ["가나다", "라마바", "사아자"]
for member in members:
    if member == keyword:
        print(member)
# 06. 리스트에서 특정 인덱스 요소 출력
members = ["가나다", "라마바", "사아자"]
target = members[1]
print(target)
# 07. 입력 받은 인덱스로 요소 접근
idx = int(input())
members = ["가나다", "라마바", "사아자"]
target = members[idx]
print(target)
# 08. 전체 목록 번호와 함께 출력
members = ["가나다", "라마바", "사아자"]
for idx, member in enumerate(members):
    print(idx,member)