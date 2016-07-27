import re
##List of all the sequences
L =['AYLMNKVVNVVEGKV', 'CDILCHWCKRNVGWK', 'CHWCKRNVGWKYLQS', 'CKRNVGWKYLQSSND','CRHCKTHLSSSFQII','DDQQYKEGKFILELK','DILCHWCKRNVGWKY','DQQYKEGKFILELKN','DYLVCDILCHWCKRN','DYRGRTGTAYLMNKV','EGKFILELKNICKCT','ENPLSSPSSSYKSIN','EQRRMLTGDYLVCDI','FHSQHRSQKNVSFIT','FITYGCRHCKTHLSS','GDYLVCDILCHWCKR','GKVEQRRMLTGDYLV','GLRYSIYIENPLSSP','GRTGTAYLMNKVVNV','GTAYLMNKVVNVVEG','HCKTHLSSSFQIISR','HLSSSFQIISRDYRG','IISRDYRGRTGTAYL','ISRDYRGRTGTAYLM','ITYGCRHCKTHLSSS','IYIENPLSSPSSSYK','KEGKFILELKNICKC','KRNVGWKYLQSSNDD','KSINDPLFHSQHRSQ','KVEQRRMLTGDYLVC','KVVNVVEGKVEQRRM','KYLQSSNDDQQYKEG','LFHSQHRSQKNVSFI','LMNKVVNVVEGKVEQ','LQSSNDDQQYKEGKF','LSSPSSSYKSINDPL','LSSSFQIISRDYRGR','LTGDYLVCDILCHWC','LVCDILCHWCKRNVG','MGLRYSIYIENPLSS','MNKVVNVVEGKVEQR','NDDQQYKEGKFILEL','NDPLFHSQHRSQKNV','NKVVNVVEGKVEQRR','NPLSSPSSSYKSIND','NVVEGKVEQRRMLTG','PLSSPSSSYKSINDP','PSSSYKSINDPLFHS','QHRSQKNVSFITYGC','QIISRDYRGRTGTAY','QKNVSFITYGCRHCK','QYKEGKFILELKNIC','RDYRGRTGTAYLMNK','RGRTGTAYLMNKVVN','RHCKTHLSSSFQIIS','RMLTGDYLVCDILCH','RRMLTGDYLVCDILC','RSQKNVSFITYGCRH','RTGTAYLMNKVVNVV','RYSIYIENPLSSPSS','SFITYGCRHCKTHLS','SINDPLFHSQHRSQK','SIYIENPLSSPSSSY','SPSSSYKSINDPLFH','SQHRSQKNVSFITYG','SQKNVSFITYGCRHC','SRDYRGRTGTAYLMN','SSFQIISRDYRGRTG','SSNDDQQYKEGKFIL','FQIISRDYRGRTGTA','SSPSSSYKSINDPLF','SSSFQIISRDYRGRT','SSSYKSINDPLFHSQ','SSYKSINDPLFHSQH','SYKSINDPLFHSQHR','TAYLMNKVVNVVEGK','TGTAYLMNKVVNVVE','THLSSSFQIISRDYR','TYGCRHCKTHLSSSF','VCDILCHWCKRNVGW','VGWKYLQSSNDDQQY','VNVVEGKVEQRRMLT','VSFITYGCRHCKTHL','VVEGKVEQRRMLTGD','VVNVVEGKVEQRRML','WKYLQSSNDDQQYKE','YGCRHCKTHLSSSFQ','YKEGKFILELKNICK','YKSINDPLFHSQHRS','YLMNKVVNVVEGKVE','YLQSSNDDQQYKEGK','YLVCDILCHWCKRNV','YRGRTGTAYLMNKVV','YSIYIENPLSSPSSS','MLTGDYLVCDILCHW']
n = 0
##start with MGLR as it does not appear in any other sequence
final = 'MGLR'
##initialize s to use later
s = ''
##This was to have a counter - i scrapped this idea
##for i in range(0,len(s)):
##    if len(re.findall(s[i:i+2],s)) == 1:
##        final += s[i:i+2]
##        i+=1
##    elif s[i:i+2] == s[i+2:i+4]:
##        final += s[i:i+2]
##        i += 2

##for loop that iterates through and returns the value of the very first 15 characters 
for n in L:
    s = n
    for i in range (0,len(s)):
        
        if s[i:i+4] == "MGLR":
            
            final+=s[i+4:len(s)]
##starting string below, following two loops check for overlap conditions ex. last 4 characters in 'final' matching witn the first 4 of some element n in list L
##there are 6 overlap conditions
s2 = "MGLRYSIYIENPLSS"
for n in L:
    s = n
    
    if s[0:4]==s2[11:15]:
        s2 = n
        
        final+=s[4:len(s)]
    if s[0:3]==s2[12:15]:
        s2 = n
        
        final+=s[3:len(s)]
    if s[1:5]==s2[11:15]:
        s2 = n
        
        final+=s[5:len(s)]
    
        continue
for n in L:
    s = n
    
    if s[0:4]==s2[11:15]:
        s2 = n
        
        final+=s[4:len(s)]
    if s[0:3]==s2[12:15]:
        s2 = n
        
        final+=s[3:len(s)]
    if s[1:5]==s2[11:15]:
        s2 = n
        
        final+=s[5:len(s)]
    
        continue
    
##This is to find the final sequence
for n in L:
    s = n
    for i in range(0,len(s)):
        if s[i:i+3]==final[len(final)-3:len(final)]:
            final+=s[i+3:len(s)]
##making sure nothing extra is printed
for n in L:
    s = n
    for i in range (0,len(s)):
        if s in final:
            continue

print (final)


