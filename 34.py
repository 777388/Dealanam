import sys
i = 0
tagged = ""
encrypt = []
for letter in sys.argv[1]:
    if (i % 2 == 0 and i != 0):
        tagged += letter
    if (i % 3 == 0 and i != 0):
        tagged += letter
    if (len(tagged) == 2):
        for letters in tagged:
            encrypt.append(letters)
        if (ord(encrypt[1]) + ord(encrypt[0]) - 96 > 0):
            (lambda: print(chr(ord(encrypt[1]) + (ord(encrypt[0])-96)), end=""))()
        else:
            (lambda: print(chr(ord(encrypt[1]) + (ord(encrypt[0])))))()
        (lambda: print(chr(ord(encrypt[1]) + (ord(encrypt[0])-96)), end=""))()
        encrypt = []
        tagged = ""
    elif(len(tagged) == 1):
        continue
    elif(len(tagged) == 0):
        print(letter, end="")
    i+=1
    
