class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                
                last_open = stack.pop()
                if last_open != hashmap[c]:
                    return False
        return len(stack) == 0



            
            
        