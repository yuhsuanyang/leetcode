def intToList(x):
    s=str(x)
    l=[]
    size=len(s)
    for i in range(size):
        l.append(int(s[i]))
    if size<4:
        c=4-size
        for i in range(c):
            l.insert(0,0)
    return l

d=[{1:'M'},{1:'C',4:'CD',5:'D',9:'CM'},{1:'X',4:'XL',5:'L',9:'XC'},{1:'I',4:'IV',5:'V',9:'IX'}]

class Solution(object):
    def intToRoman(self, num):
        n=intToList(num)
        ans=[]
        for i in range(4):
            if n[i]==0:
                ans.append('')
            elif n[i]==4 or n[i]==9:
                ans.append(d[i].get(n[i]))
            else:
                a=round(int(n[i])/5)
                b=int(n[i])%5
                if a==1:
                    ans.append(d[i].get(5))
                for j in range(b):
                    ans.append(d[i].get(1))
        result=''.join(ans)
        return result
                
sol=Solution()
s=1994
sol.intToRoman(s)
