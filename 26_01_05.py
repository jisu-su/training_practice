# 클라우드가 만들어준 추가 연습
# 주석 보고 만들기 (challenge)
# 1. 영화 3개 입력 받고 번호와 함께 출력
# 1-1. 빈 리스트 movies 만들기
movies = []
# 1-2. 3번 반복하면서 영화 제목 입력 받아 추가하기
for i in range(3):
    movie = input()
    movies.append(movie)
    # 1-3. enumerate 사용해서 번호와 함께 출력하기
for idx, movie in enumerate(movies):
    print(idx+1, movie)