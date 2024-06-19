def solution(n, slicer, num_list):
    answer = []
    sr = Slice_Rule(*slicer)
    
    return sr.get(num_list, n)

class Slice_Rule:
    def __init__(self, a, b, c):
        self.rule = {
            1: slice(b+1),
            2: slice(a,None),
            3: slice(a,b+1),
            4: slice(a,b+1,c)
        }
    def get(self, item: list, n):
        return item[self.rule[n]]