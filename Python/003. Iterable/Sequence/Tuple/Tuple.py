# Tuple은 몇 가지 점을 제외하고는 List와 거의 비슷하다.
# 1. 리스트는 [과 ]로 둘러싸지만 튜픙른 (과 )로 둘러싸임
# 2. 튜플은 값의 변경이 불가능하다.

# Tuple 예시
t1 = ()
t2 = (1,)
# 요소 값이 1개일 때 ,를 붙여주지 않으면 t2는 값이 1인 int형 변수가 됨.
t3 = (1, 2, 3)
t4 = 1, 2, 3
# 괄호를 생략해도 무방함.
t5 = ('a', 'b', ('ab', 'cd'))
# Tuple 안의 Tuple


# -- Tuple 에서의 인덱싱과 슬라이싱
t1 = (1, 2, 3, 4)
print(t1[2])
# 3 출력

print(t1[:2])
# (1, 2) 출력

# 튜플 더하기
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)
# (1, 2, 3, 4)

# 튜플 곱하기
print(t1 * 3)
# (1, 2, 1, 2, 1, 2)
# t1의 값을 3번 반복한 값을 리턴 해준다.