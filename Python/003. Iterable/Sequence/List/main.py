# 반복 가능한 자료형을 iterable 자료형이라고 하며 순서가 존재한다.

l = [1, 2, 3, 4, 5, 6]
# 다른 언어에서의 배열과 비슷한 형태를 하고 있음

# 배열(Array)과 다른 점은,
# 배열에서는 인덱스에 따라 값을 유지하기 때문에 빈 자리가 남게 된다.
# 하지만 List는 중간에 빈 부분이 있으면 뒤에 인덱스의 값이 앞으로 와서 빈틈없이 연속적으로 위치한다.

# -- 인덱스가 중요한 경우는 배열을 사용, 인덱스가 중요하지 않은 경우에는 리스트를 사용한다.


# 요소 추가
l.append(7)
# 리스트의 맨 끝에 7이라는 값 추가

l.insert(1, 10)
# 1번 인덱스의 값을 10으로 변경


# 인덱싱
l[1] = 10
l[-1] = 9
# Python에서 -1번 인덱스는 맨 뒤에서 첫번째의 위치를 의미함
# [1, 2, 3, 4, 5] 일 때, 5는 4번 인덱스, -1번 인덱스 두 개로 표현 가능함


# 슬라이싱
print(l[1:3])
# 특정 값을 잘라내기 위해 사용한다.
# 슬라이싱의 기본 형태는 [start:end:stride(step)]
# start란 시작 지점, end는 지정된 값의 -1 인덱스까지. ( 9라면 8번 인덱스까지 ), stride는 슬라이싱 할 간격을 의마함

l[1:3] = [1, 2]
# 특정 값을 바꿈

print(l[:])
# 아무 숫자도 지정하지 않으면 처음부터 끝까지
print(l[1:])
# 1번 인덱스부터 끝까지
print(l[:4])
# 처음 인덱스부터 3번 까지


# 요소 제거
del l[0]
del l[:2]
# 말 그대로 delete. 값을 제거함

# 기타 메서드
l.sort()
# 낮은 순서대로 정렬, 알파벳은 아스키 코드 순서로 정렬됨.

l.reverse()
# 거꾸로

print(l.count(1))
# list 내 1의 갯수

print(l.index(2))
# 2가 최초 반환되는 지점 반환

print(l.pop())
# 리스트의 맨 마지막 값을 출력하며 삭제시킴

l.clear()
# 리스트 클리어