#function to test if a word is using only those letters
# return boolean
def WordTester(myword):
    letterList = ['b','v','c','lli','u','o','a','rr','n','\n']
    if len(letterList)==1 and letterList[0] in myword:
        return True
    else:
        for tmp in letterList[:-1]:
            if(len(tmp)>=2 and tmp in myword):
                #le mot possède le string
                NewWord = myword.replace(tmp,"")
                for letter in NewWord:
                    if not letter in letterList:
                        return False
                return True
    return False

#clean the word of the last \n
def WordCleaner(myword):
    return myword[:-1]

#test if the word is between x and y
#useful if you want a specific lenght
def ForkGrabber(x,y,word):
    if(len(word)>=x and len(word)<=y):
        return True
    else:
        return False

#export to a file.
def export(lenght, min, max):
    tmp = []
    fr = open("dicofr.txt","r",encoding="utf-8")
    exp = open('Output/export.txt',"w+",encoding="utf-8")
    for word in fr:
        word = WordCleaner(word)
        if(WordTester(word) and ForkGrabber(min, max, word)):
            tmp.append(word)
    for i in tmp:
        print(i)
    if len(tmp)<=lenght:
        for x in tmp:
            exp.write(x+" ")
    else:
        for x in tmp[0::int(len(tmp)/(lenght-1))]:
            exp.write(x+" ")
        
    exp.close()
    fr.close()

#main
export(30, 3, 12)
