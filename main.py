#function to test if a word is using only those letters
# return boolean
def WordTester(myword):
    letterList = ['a','e','i','u','s','o','v','t','n','\n']
    for letter in myword:
        if not letter in letterList:
            return False
    return True

#clean the word of the last \n
def WordCleaner(myword):
    return myword[:-1]

#test if the word is between x and y
def ForkGrabber(x,y,word):
    if(len(word)>=x and len(word)<=y):
        return True
    else:
        return False

#export to a file. couter is to know the size
def export():
    fr = open("dicofr.txt","r",encoding="utf-8")
    exp = open('Output/export.txt',"w+",encoding="utf-8")
    counter = 0
    for word in fr:
        word = WordCleaner(word)
        if(WordTester(word) and ForkGrabber(5, 7, word) and counter<60):
            exp.write(word+" ")
            counter+=1
    exp.close()
    fr.close()

#main

export()
