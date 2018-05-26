# Object id

# 변경 불가능한 타입의 객체는 내용이 같으면
# 같은 ID를 가진다.(동일한 객체이다.)

i1 = 10
i2 = 10

print(hex(id(i1)), hex(id(i2)))

# 변경 가능한 타입의 객체는 같아도
# 다른 ID를 가진다.(다른 객체이다.)

l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(hex(id(l1)), hex(id(l2)))


# str은 immutable 이다.
s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

