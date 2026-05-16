
# 클래스에 __iter__(), __next__() 메서들를 구현하면 이터레이터가 된다.
# 
class Myrange: 
    def __init__(self, n): 
        self.maxn = n
        self.current = 0

    def __iter__(self): 
        return self
    
    def __next__(self): 
        if self.current >= self.maxn: 
            raise StopIteration
        else: 
            ret = self.current
            self.current += 1
            return ret
        
int_list = Myrange(5)
for i in int_list: 
    print(i, end="") #01234

