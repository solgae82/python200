# 출석부에 넣을 학생 이름 목록입니다.
students = ["철수", "영희", "민수"]

# 1. 값(value)을 지정하지 않고 만들기
# -> 기본적으로 'None'(아무것도 없음)이 들어갑니다.
attendance_book1 = dict.fromkeys(students)
print("출석부 1번:", attendance_book1)
print("-" * 30)

# 2. 값(value)을 '출석'으로 지정해서 한 번에 만들기
# -> 모든 학생의 상태가 한 번에 '출석'으로 채워집니다.
attendance_book2 = dict.fromkeys(students, "출석")
print("출석부 2번:", attendance_book2)
