
#입력값과 리턴값 없는 함수 , return 기본: None
def displayFilePath(): 
    filepath='c:/my'
    print(f'파일경로:{filepath}')
    return

d = displayFilePath() #파일경로:c:/my
print(d) #None


#리턴문 없어도 'return' 있는 것으로 간주. 기본 None 리턴
def displayHello(): 
    print('Hello')

d2 = displayHello() # Hello
print(d2) #None


#입력값은 없고, 리턴값은 있는 함수
def getMessage(): 
    return '안녕!'

print(getMessage()) #안녕!

#입력값 있고, 리턴값 없는 함수,(return 힌트 사용)
def printMessage(msg:str) -> None: 
    print(f'Hey man! {msg}')
    return

d3 = printMessage('dong') # Hey man! dong
print(d3) # None


#입력값과 리턴값 있는 함수 (return 힌트 사용)
def getFilePath(folder , filename) -> str:
    return folder + '/' + filename

print(getFilePath('c:/my','dong_name.txt')) #c:/my/dong_name.txt
