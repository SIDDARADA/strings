s=input()
n=int(input())
news=''
for i in range(0,len(s)):
    if i!=n:
        news=news+s[i]
print(news)
