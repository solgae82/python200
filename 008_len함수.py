# len() 함수
# 모든 시퀀스 자료형과 딕셔너리, Set 등 요소 길이(크기) 반환

strData = 'I Love python!'
print('문자갯수:',len(strData)) #문자갯수: 14

listData = [1,2,3]
print('리스트요소갯수:',len(listData)) #리스트요소갯수: 3

tupleData = ('a', 'bc', 'def')
print('튜플요소갯수:',len(tupleData)) #튜플요소갯수: 3

setData = {'cup', 'shirts', 'pants','cup'}
print('Set요소갯수:',len(setData))  #Set요소갯수: 3 , [중복값은 제거된다]

dicData = {1:True, 0:False}
print('딕셔너리요소갯수:', len(dicData)) #딕셔너리요소갯수: 2