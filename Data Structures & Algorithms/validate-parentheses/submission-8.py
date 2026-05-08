class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        brkt_stack = []
        for brt in s:
            if brt in brackets.keys():
                brkt_stack.append(brt)
            else:
                if len(brkt_stack) == 0:
                    return False
                o_brt = brkt_stack.pop()
                print(brackets.get(o_brt, '!'), brt)
                if brackets.get(o_brt, '!') != brt:
                    return False
        
        return len(brkt_stack) == 0
