import os
import random
import requests
import socket as skt
import subprocess as sps

try:
    TDp = open("TranslatorDic.py")
except:
    raise ModuleNotFoundError("Translator Dic.py is required to run the program")
    os.quit
else:    
    TDp.close()
    import TranslatorDic
    
    username = skt.gethostname()
    
    Trans = TranslatorDic
    
    decimal =""
    binary=""
    reverseword = ""
    combination = ""
    sum = 0
    mctt =""
    
    dr = input("Enter word/number: ")
    
    inpwordar = [str(x) for x in dr]
    larr = len(inpwordar)
    larrnospace = larr - inpwordar.count(' ')
    
    for revletter in reversed(inpwordar):
        reverseword += revletter
    
    for mclt in inpwordar:
        sum = sum - 1
        combination += mclt
        combination += inpwordar[sum]
        binar = str(bin(ord(mclt)))
        binary += binar.replace("0b","")+" "
        decimal += str(ord(mclt))+" "
        if mclt in Trans.MorseTran:
            mcul = mclt
            mcpl = Trans.MorseTran.get(mcul)
            mctt += mcpl+"/"
        else:
            mctt += "[UC]"+"/"
            
    randnumrun = random.randint(0, 255)
    
    try:
        os.remove("outputfile.txt")
    finally:
        tempfile1o = open("outputfile.txt","at")
        tempfile1o.write("Welcome ")
        tempfile1o.write(str(username))
        tempfile1o.write("\n")
        tempfile1o.write("\n")
        tempfile1o.write("Array: ")
        tempfile1o.write(str(inpwordar))
        tempfile1o.write("\n")
        tempfile1o.write("Length of word: ")
        tempfile1o.write(str(larr))
        tempfile1o.write("\n")
        tempfile1o.write("Length of word with no spaces: ")
        tempfile1o.write(str(larrnospace))
        tempfile1o.write("\n")
        tempfile1o.write("Given word reveresed: ")
        tempfile1o.write(str(reverseword))
        tempfile1o.write("\n")
        tempfile1o.write("Combination of the word, following a back front back front pattern: ")
        tempfile1o.write(str(combination))
        tempfile1o.write("\n")
        tempfile1o.write("Morse code of given word: ")
        tempfile1o.write(mctt)
        tempfile1o.write("\n")
        tempfile1o.write("Decimal of given word: ")
        tempfile1o.write(decimal)
        tempfile1o.write("\n")
        tempfile1o.write("Binary of given word: ")
        tempfile1o.write(str(binary))
        tempfile1o.write("\n")
        tempfile1o.write("Random Number of this run is: ")
        tempfile1o.write(str(randnumrun))
        tempfile1o.write("\n")
        tempfile1o.close()
        
        url = 'https://www.richfield.ac.za/'
        
        try:
            req1 = requests.get(url)
            reqc = req1.cookies
            reqsc = req1.status_code
            reqte = req1.elapsed
            reqenc = req1.encoding
            reqh = req1.headers
        except:
            raise Exception("Unable to find site")
        else:
            tempfile1o = open("outputfile.txt","at")
            tempfile1o.write("\n")
            tempfile1o.write("URL: ")
            tempfile1o.write(str(url))
            tempfile1o.write("\n")
            tempfile1o.write("Cookies: ")
            tempfile1o.write(str(reqc))
            tempfile1o.write("\n")
            tempfile1o.write("Status code: ")
            tempfile1o.write(str(reqsc))
            tempfile1o.write("\n")
            tempfile1o.write("Request time: ")
            tempfile1o.write(str(reqte))
            tempfile1o.write("\n")
            tempfile1o.write("Encoding: ")
            tempfile1o.write(str(reqc))
            tempfile1o.write("\n")
            tempfile1o.write("Headers: ")
            tempfile1o.write(str(reqh))
            tempfile1o.write("\n")
            tempfile1o.close()
            sps.run(["python",""])