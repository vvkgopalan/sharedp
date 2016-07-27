# sharedp
import re
L = ['SQTAP', 'APALT', 'TAPAL']
n = 0
final = 'SQ'
s = ''
##for i in range(0,len(s)):
##    if len(re.findall(s[i:i+2],s)) == 1:
##        final += s[i:i+2]
##        i+=1
##    elif s[i:i+2] == s[i+2:i+4]:
##        final += s[i:i+2]
##        i += 2

for i in range (0,len(L[1])):
    s = L[1]
    if s[i:i+2] == "SQ":
        final += s[i+2:i+3]
        final+=s[i+3:len(s)]
for i in range (0,len(L[2])):
    if L[2][i:i+2]==L[1][3:5]:
        match = L[2][i:i+2]
        
        final+=L[2][i+2:len(s2)]
for n in L:
    s = n
    for i in range (0,len(s)):
        if s in final:
            break

print (final)


