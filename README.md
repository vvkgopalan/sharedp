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
s = L[0]
for i in range (0,len(s)):
    
    if s[i:i+2] == "SQ":
        final += s[i+2:i+3]
        final+=s[i+3:len(s)]

s = L[1]
for i in range (0,len(s)):
    if s[i:i+2]==L[0][3:5]:
        match = s[i:i+2]
        
        final+=s[i+2:len(s)]
for n in L:
    s = n
    for i in range (0,len(s)):
        if s in final:
            break

print (final)


