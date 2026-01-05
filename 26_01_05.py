# 클라우드가 만들어준 추가 연습
# 1. 기본 흐름 익히기
movies = []
movies.append("쉐이프 오브 워터")
movies.append("라라랜드")
movies.append("인터스텔라")

for movie in movies:
    print(movie)

# 2. enumerate 익히기
movies = ["쉐이프 오브 워터", "라라랜드", "인터스텔라"]

for idx, movie in enumerate(movies):
    print(f"{idx + 1}. {movie}")

# 3. pop 익히기
movies = ["쉐이프 오브 워터", "라라랜드", "인터스텔라"]
# *pop은 ()안에 아무것도 안 적혀 있으면 마지막 요소를 삭제한다.
deleted = movies.pop()
print(f"삭제된 영화: {deleted}")
print(f"남은 영화: {movies}")

# 4. 입력 받아 추가하기
movies = []
# *movies로 빈 바구니를 먼저 만들고 range로 3번 반복
for i in range(3):
    movie = input("영화 제목: ")
    movies.append(movie)
print("등록된 영화:", movies)

# 5. 검색하기
movies = ["쉐이프 오브 워터", "라라랜드", "인터스텔라"]
keyword = input("찾을 영화: ")

for movie in movies:
    if movie == keyword:
        print(f"찾았습니다: {movie}")
