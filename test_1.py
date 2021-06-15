# Title Banner
print(" " +"-"*20+"| Simple Substitution Cipher |"+"-"*20+" ")

# Obtain user input
key=input(" > Key?\n| ");subject=input(" Subject?\n| ")

# Init runtime variables
keycode=[];subcode=[];endcode=[];import string;listof=string.printable+" ";end=""

# Convert input 'key' to array of integers
for i in key:
    keycode.append(listof.find(i))

# Convert input "subject" to array of integers
for i in subject:
    subcode.append(listof.find(i))

# Extend 'keycode' array to be long enough to not cause IOOR errors
keycode = keycode*15

# Apply key values to subject values
for i in subcode:
    endcode.append(i+keycode[subcode.index(i)])

# Extract string from the resulting array of integers
for i in endcode:
    end=end+listof[i]

# Print result
print(end)
