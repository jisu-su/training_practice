# 클라우드가 만들어준 추가 연습
# 주석 보고 만들기 (challenge)
# 1. 영화 3개 입력 받고 번호와 함께 출력
# # 1-1. 빈 리스트 movies 만들기
# movies = []
# # 1-2. 3번 반복하면서 영화 제목 입력 받아 추가하기
# for movie in range(3):
#     movie = input()
#     movies.append(movie)
# # 1-3. enumerate 사용해서 번호와 함께 출력하기
# for idx, movie in enumerate(movies):
#     print(f"{idx + 1}. {movie}")

# # 2. 마지막 영화 삭제하고 확인 메세지
# # 2-1. 영화 리스트 만들기 (3개)
# movies = ["쉐이프 오브 워터", "라라랜드", "인터스텔라"]
# # 2-2. 전체 영화 출력하기
# print(movies)
# # 2-3. 마지막 영화를 pop으로 삭제하고 deleted 변수에 저장
# deleted = movies.pop()
# # 2-4. "삭제된 영화: __" 출력
# print(f"삭제된 영화: {deleted}")
# # 2-5. 남은 영화 목록 출력
# print(f"남은 영화: {movies}")

# 3. 영화 검색 (부분 일치)
# 3-1. 영화 리스트 만들기
movies = ["쉐이프 오브 워터", "라라랜드", "인터스텔라"]
# 3-2. 검색어 입력받기
search = input()
# 3-3. 모든 영화를 확인하면서 
for movie in movies:
# 3-4. 검색어가 포함된(in) 영화만 출력
    if search in movies:
        print(f"찾을 영화: {search}")
print(f"찾았습니다: {movies}")