class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        result = ""
        carry = 0
        for i in range(n-1, -1, -1):
            if a[i] == '1': carry += 1
            if b[i] == '1': carry += 1
            
            if carry % 2 == 1:
                result += '1'
            else: 
                result += '0'
            carry //= 2
        
        if carry == 1:
            result += '1'
        return result[::-1]

print(Solution().addBinary('1111', '10'))