# 내장 함수

# abs
# abs(x)는 어떤 숫자를 입력으로 받았을 때,그 숫자의 절대값(양의 정수)을 돌려주는 함수이다.

print("\nabs(x)\n")

abs(3)
print(abs(3))

abs(-3)
print(abs(-3))

abs(-1.2)
print(abs(-1.2))

# all
# all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며, 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴한다.

print("\nall(x)\n")

all([1, 2, 3])
print(all([1, 2, 3]))

all([1, 2, 3, 0])
print(all([1, 2, 3, 0]))

# any
# any(x)는 x 중 하나라도 참이 있을 경우 True를 리턴하고, x가 모두 거짓일 경우에만 False를 리턴한다.

print("\nany(x)\n")

any([1, 2, 3, 0])
print(any([1, 2, 3, 0]))

any([0, ""])
print(any([0, ""]))

# chr
# chr(i)는 아스키(ASCII) 코드값을 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수이다.

print("\nchr(i)\n")

chr(97)
print(chr(97))  # ASCII CODE 97 = a

chr(48)
print(chr(48))  # ASCII CODE 48 = 0

# dir
# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다. 아래 예는 리스트와 딕셔너리 객체의 관혐 함수들(메서드)들을 보여주는 예이다.

print("\ndir\n")

dir([1, 2, 3])
print(dir([1, 2, 3]))

dir({'1': 'a'})
print(dir({'1': 'a'}))

# divmod
# divmod(a,b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태()로 리턴하는 함수이다.

print('\ndivmod\n')

divmod(7, 3)
print(divmod(7, 3))

divmod(1.3, 0.2)
print(divmod(1.3, 0.2))

# enumerate
# enumerate는 '열거하다'라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함한
# enumerate 객체를 리턴한다.

print('\nenumerate\n')

if __name__ == '__main__':
    for i, name in enumerate(['body', 'foo', 'bar']):
        print(i, name)

# 순서값과 함께 body, foo, bar가 순서대로 출력되었다. 즉, 위 예제와 같이 enumerate를 for문과 함께 사용하면 자료형의 현재 인덱스(index)와 그 값을 쉽게 알 수 있다.

# eval
# eval(expression)은 실행 가능한 문자열(1+2,'hi'+'a'같은 것)을 입력으로 받아 문자열을 실행한 결과값을 리턴하는 함수이다
# 보통 eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶은 경우에 사용된다.

print('\neval\n')

eval('1+2')
print(eval('1+2'))

eval("'hi' + 'a'")
print(eval("'hi' + 'a'"))

eval('divmod(4,3)')
print(eval('divmod(4,3)'))

# filter
# filter란 무엇인가를 걸러낸다는 뜻으로, filter 함수도 동일한 의미를 가진다.
# filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복가능한 자료형을 받는다.
# 그리고 두번째 인수인 반복 가능한 자료형 요소들이 첫 번째 인수인 함수에 입력되었을 떄 리턴 값이 참인 것만 묶어서(걸러내서) 돌려준다

print("\nfilter\n")


def positive(numberList):
    result = []  # 리턴값이 참인 것만 걸러내서 저장할 변수
    for num in numberList:
        if num > 0:
            result.append(num)
    return result


print(positive([1, -3, 2, 0, -5, 6]))


def positive(x):
    return x > 0


print(list(
    filter(
        positive, [1, -3, 2, 0, -5, 6]
    )
)
)

# hex
# hex(x) 정수값을 입력받아 16진수(hexadecimal)로 변환하여 리턴하는 함수이다.

print("\nhex(x)\n")

hex(234)
print(hex(234))

hex(3)
print(hex(3))

# id
# id(object)는 객체를 입력받아 객체의 고유 주소값(레퍼런스)를 리턴하는 함수이다.


a = 3  # 모두 같은 객체를 가리킨다.
id(3)
print(id(3))
id(a)
print(id(a))
b = a
id(b)
print(id(b))

id(4)
print(id(4))

# input
# input([prompt])은 사용자 입력을 받는 함수이다.
# 입력 인수롬 ㅜㄴ자열을 주면 아래의 세 번째 예에서 볼 수 있듯이 그 문자열은 프롬프트가 된다.

# [] 기호는 괄호안의 내용을 생략할 수 있다는 관례적 표기법이다.
# 파이썬 2.7버전의 경우 input 대신 raw_input을 사용해야 한다.

print("\ninput\n")

# a = input() # 사용자가 입력한 정보를 변수 a에 저장
print(a)

# b = input("Enter: ")  # Enter:라는 프롬프트를 띄우고 사용자 입력을 받음
print(b)

# int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 리턴하는 함수로, 정수를 입력으로 받으면 그대로 리턴한다.

print("\nint\n")

int('3')
print(int('3'))

int(3.4)
print(int(3.4))

# int(x,radix)는 radix 진수로 표현된 문자열 s를 10진수로 변환하여 리턴한다.

print("\nint(x,radix)\n")

int('11', 2)  # 2진수 11을 10진수로 변환
print(int('11', 2))

int('1A', 16)
print(int('1A', 16))  # 16진수 1A를 10진수로 변환

# isinstance
# isinstance(object,class)는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거지이면 False를 리턴한다.

print("\nisinstance\n")


class Person: pass  # 아무 기능이 없는 Person 클래스 생성


a = Person()  # Person 클래스의 인스턴스 a 생성
isinstance(a, Person)  # a가 Person 클래스의 인스턴스인지 확인
print(isinstance(a, Person))

b = 3
isinstance(b, Person)
print(isinstance(b, Person))

# lambda
# lambda는 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다. 보통 함수를 한줄로 간결하게 만들 떄 사용한다.
# def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.

# lambda 인수1, 인수2 ... : 인수를 이용한 표현식

print("\nlambda\n")

sum = lambda a, b: a + b
sum(3, 4)
print(sum(3, 4))


def sum(a, b):
    return a + b


myList = [lambda a, b: a + b, lambda a, b: a * b]
print(myList)  # 리스트 myList에 람다 함수가 2개 추가됨.

myList[0]
print(myList[0])
print(myList[0](3, 4))

myList[1]
print(myList[1])
print(myList[1](3, 4))

# len
# len(s)은 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수이다.

print("\nlen\n")

len("python")
print(len("python"))

len([1, 2, 3])
print(len([1, 2, 3]))  # 리스트

len((1, 'a'))
print(len((1, 'a')))  # 튜플

# list
# list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 리턴하는 함수이다.

print("\nlist\n")

list("python")
print(list("python"))
list((1, 2, 3))
print(list((1, 2, 3)))

a = [1, 2, 3]
b = list(a)
print(b)

# map
# map(f,iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력 받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수이다.

print("\nmap\n")


def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result


result = two_times([1, 2, 3, 4])
print(result)


def two_times(x): return x * 2


list(map(two_times, [1, 2, 3, 4]))
print(list(map(two_times, [1, 2, 3, 4])))

list(map(lambda a: a * 2, [1, 2, 3, 4]))
print(list(map(lambda a: a * 2, [1, 2, 3, 4])))

# max
# max(ierable)는 인수로 반복 가능한 자료형을 입력받아 그 최대갑을 리턴한다.

print("\nmax\n")

max([1, 2, 3])
print(max([1, 2, 3]))

max("python")
print(max("pyhon"))

# min
# min(iterable)은 max 함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최소값을 리턴하는 함수이다.

print("\nmin\n")

min([1, 2, 3])
print(min([1, 2, 3]))

min("python")
print(min("python"))

# oct
# oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 리턴하는 함수이다.

print("\noct(x)\n")

oct(34)
print(oct(34))

oct(12345)
print(oct(12345))

# open
# open(filename, [mode])은 '파일 이름'과 '읽기 방법'을 입력받아 파일 객체를 리턴하는 함수이다. 읽기 방법(mode)이 생략되면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 리턴한다.

# w : 쓰기 모드로 파일 열기
# r : 읽기 모드로 파일 열기
# a : 추가 모드로 파일 열기
# b : 바이너리 모드로 파일 열기

print("\nopen\n")

# b는 w,r,a와 함께 사용된다.
# f = open("binary_fiel", "rb")

# fread = open("read_mode.txt", "r")
# fread2 = open("read_mode.txt")

# ord
# ord(c)는 문자의 아스키 코드값을 리턴하는 함수이다.
# ord(c) 함수는 chr함수와는 반대이다.

print("\nord\n")

ord('a')
print(ord('a'))

ord('0')
print(ord('0'))

# pow
# pow(x,y)는 x의 y 제곱한 결과값을 리턴하는 함수이다.

print('\npow\n')

pow(2, 4)  # 2의 4 제곱
print(pow(2, 4))

pow(3, 3)  # 3의 3제곱
print(pow(3, 3))

# range
# range([start,]stop[,step])는 for문과 함께 자주 사용되는 함수이다. 이 함수는 입력받은 숫자에 해당되는 범위의 값을 반복 가능한 객체로 만들어 리턴한다.

print("\nrange\n")

# 인수가 하나일 경우
# 시작 숫자를 지정해주지 않으면 range 함수는 0부터 시작한다.

list(range(5))
print(list(range(5)))

# 인수가 2개일 경우
# 입력으로 주어지는 2개의 이누는 시작 숫자와 끝 숫자를 나타낸다. 단, 끝 숫자는 해당 범위에 포함되지 않는다는 것을 주의

list(range(5, 10))
print(list(range(5, 10)))  # 끝 숫자 10은 포함되지 않음

# 인수가 3개일 경우
# 세번째 인수는 숫자 사이의 거리를 말한다.

list(range(1, 10, 2))
print(list(range(1, 10, 2)))  # 1부터 9까지, 숫자 사이의 거리는 2

list(range(1, -10, -1))
print(list(range(1, -10, -1)))  # 0부터 -9까지, 숫자 사이의 거리는 -1

# sorted
# sorted(ierable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 리턴하는 함수이다.

print("\nsorted\n")

sorted([3, 1, 2])
print(sorted([3, 1, 2]))

sorted(['a', 'c', 'b'])
print(sorted(['a', 'c', 'b']))

sorted("zero")
print(sorted("zero"))

# 리스트 자료형에도 sort라는 하무가 있다. 하지만 자료형의 sort 함수는 리스트 객체 그 자체를 정렬만 할 뿐 정렬된 결과를 리턴하지는 않는다.

a = [3, 1, 2]
result = a.sort()
print(result)

# str
# str(object)은 문자열 형태로 객체를 변환하여 리턴하는 함수이다.

str(3)
print(str(3))
str('hi')
print(str('hi'))
str('hi'.upper())
print(str('hi'.upper()))

# tuple
# tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 리턴하는 함수이다. 만약 튜플이 입력으로 들어오면 그대로 리턴한다.

print("\ntuple\n")

tuple("abc")
print(tuple("abc"))

tuple([1, 2, 3])
print(tuple([1, 2, 3]))

tuple((1, 2, 3))
print(tuple((1, 2, 3)))

# type
# type(object)은 입력값의 자료형이 무엇인지 알려주는 함수이다.

print("\ntype\n")

type("abc")
print(type("abc"))  # "abc" 문자열 자료형(str)

type([])
print(type([]))  # []은 리스트 자로형(list)

type(open("test", 'w'))
print(type(open("test", 'w')))  # 파일 자료형 io.TextIOWrapper

# zip
# zip(iterable)은 동일한 개ㅜ로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다. 잘 이해 되지 않는다면 다음 예제를 살펴보자

print("\nzip\n")

list(zip([1, 2, 3], [4, 5, 6]))
print(list(zip([1, 2, 3], [4, 5, 6])))

list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))

list(zip("abc", "def"))
print(list(zip("abc", "def")))
