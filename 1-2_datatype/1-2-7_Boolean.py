# 자료형의 참과 거짓

# 문자열, 리스트, 튜플 딕셔너리 등의 값이 비어있으면 거짓이 된다.
# 숫자형은 0이 아닌 숫자면 참이고, 0이면 거짓이다.
# None도 거짓이다.

a = [1, 2, 3, 4]
while a: # a가 참인 동안
    a.pop() # 리스트의 마지막 요소를 반환한 후 요소 삭제하는 함수

#while 조건문:
#   처리할 수행식

if [] : #만약 []가 참이면
    print("True") # True라는 문자열 출력
else: #만약 []가 거짓이면
    print("False") #False라는 문자열 출력

if[1,2,3]:
    print("True")
else:
    print("False")
