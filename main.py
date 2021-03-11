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
    for x in tmp[0::int(len(tmp)/(lenght-1))]:
        exp.write(x+" ")
    exp.close()
    fr.close()

#main
export(15, 5, 8)
