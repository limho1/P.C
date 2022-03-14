'''
2022_03_14
2주차 수업
'''
'''
print('hello');
print("hello")

print("He's name is 철수")
print('He said "I am OK"')

print("He said \"I am OK\" ")
print("a" * 10)
'''
print("="*30,"\nHe said \"Python is Easy\"","\n34256곱하기2365는",34256*2365,"입니다\n","="*30)

'''
print("A")
print("B")
print("A\nBC\nDEF") #\n은 new line을 의미
'''
'''
#=====문자열 슬라이싱(slice)====
#print("Hello"[0])
#print("Hello"[1])
print("Hello"[-1]) #뒤에서 첫 글자
print("Hello"[0:3]) #0<= 범위 <3 출력
'''
'''
a=input() #a는 입력된 숫자를 가리킴
print(a) #a가 가리키는 것을 출력
'''
'''
b=input("오늘 날짜입력:");
print(b[0:4],"\n",b[5:7],"\n",b[8:10])

a=input("현재 연도 입력:");
b=input("태어난연도입력:");

#나이 출력하기
print('당신의 한국 나이는',int(a)-int(b)+1,'살\n만 나이는',int(a)-int(b),'살 입니다')  

a= 1333;
a= 123;
a= a+100;
print(a)
a-=3; #a가 가리키는 값에서 3을 뺌
a+=3;

b=100;
b*=4;
print(b)
a=100;
b=2;
c=2;
print(a+b*c) #예상되는 결과값 : 104
print((a+b)*c) #예상되는 결과값 : 204
'''
a=int(input("첫번째숫자입력:"));
b=int(input("두번째숫자입력:"));
print("더한결과:",a+b)
print("곱한결과:",a*b)
print("뺀결과:",a-b)

