"""
아무것도 실행하지 않는 코드를 넣을때 사용하는 'pass' 키워드
나중에 코드를 넣기 위해 임시로 사용한다.
"""

x = 0
if x == 0: pass

for sport in ['축구', '야구','배구']:
    if sport == '축구':
        pass
    if sport == '야구': print('야구 있다') #야구 있다


def getLink(url):
    pass

getLink('http://google.com') #아무일도 하지 않는다
