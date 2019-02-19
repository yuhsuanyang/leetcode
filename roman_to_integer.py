class Solution(object):
    def romanToInt(self, s):
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l=['IV','IX','XL','XC','CD','CM']
        ans=0
        i=0
        while(i< len(s)):
            if s[i:i+2] in l:
                num=s[i:i+2]
                x=d.get(num[1])-d.get(num[0])
                i=i+2
            else:
                x=d.get(s[i])
                i=i+1
            ans=ans+x
        return ans
    
    
s="MCMXCIV"
sol=Solution()
sol.romanToInt(s)


