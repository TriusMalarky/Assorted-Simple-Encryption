print(" " +"-"*20+"| Simple Substitution Cipher |"+"-"*20+" ")
key=input(" > Key?\n| ");subject=input(" Subject?\n| ")
keycode=[];subcode=[];import string;endcode=[]
for i in key:
    keycode.append(string.printable.find(i))
for i in subject:
    subcode.append(string.printable.find(i))
keycode = keycode*15
for i in subcode:
    endcode.append(i+keycode[subcode.index(i)])
end=""
for i in endcode:
    end=end+string.printable[i]
print(end)
