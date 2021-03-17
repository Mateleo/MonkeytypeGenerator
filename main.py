# function to test if a word is using only those letters
# return boolean
def WordTester(myword):
    # letterList = ['b','v','c','lli','u','o','a','rr','n','\n']
    letterList = ['u', 'r', 't', 'o', 's', 'i',
                  'e', 'o', 'v', 'n', 'm', 'c', 'é', 'a', 'd','f']
    if len(letterList) == 1 and letterList[0] in myword:
        return True
    else:
        for tmp in letterList:
            if(len(tmp) >= 2 and tmp in myword):
                # le mot possède le string
                myword = myword.replace(tmp, "")
            for letter in myword:
                if not letter in letterList:
                    return False
            return True
    return False

# clean the word of the last \n


def WordCleaner(myword):
    return myword[:-1]

# test if the word is between x and y
# useful if you want a specific lenght


def ForkGrabber(x, y, word):
    if(len(word) >= x and len(word) <= y):
        return True
    else:
        return False

# export to a file.
def export(lenght, min, max):
    tmp = []
    wordlist = []
    ranklist = []
    sentencelist = []
    score = []
    fr = open("Data/exemple.txt", "r", encoding="utf-8")
    exp = open("Output/export.txt", "w+", encoding="utf-8")
    for sentence in fr:
        wordlist = SentenceToWord(sentence)
        rank = ranker(sentence, min, max)
        if rank != 0:
            ranklist.append(rank)
            sentencelist.append(wordlist)
            score.append(len(wordlist)/rank)
        for word in wordlist:
            if(WordTester(word) and ForkGrabber(min, max, word)):
                tmp.append(word)
    Z = [x for _, x in sorted(zip(score, sentencelist))]
    print("-------")
    for x in range(0, 8):
        print(Z[x])

    print(sorted(score, reverse=True)[-8:])
    print("-------")
    V = [x for _, x in sorted(zip(ranklist, sentencelist))]
    for x in range(1, 6):
        print(V[-x])
    print(sorted(ranklist)[-5:])
    # print(V[-5:])
    # for i in tmp:
    #     print(i)
    if len(tmp) <= lenght:
        for x in tmp:
            exp.write(x+" ")
    else:
        for x in tmp[0::int(len(tmp)/(lenght-1))]:
            exp.write(x+" ")

    exp.close()
    fr.close()


def SentenceToWord(mystr):
    a = ""
    b = []
    for word in mystr:
        if word != " " and word != "\n":
            a += word
        else:
            b.append(a)
            a = ""
    return b


def ranker(sentence, min, max):
    rank = 0
    mylist = SentenceToWord(sentence)
    word = mylist[rank]
    while (WordTester(word) and ForkGrabber(min, max, word)):
        rank += 1
        if rank == len(mylist):
            return rank
        word = mylist[rank]
    return rank


def rankerSoft(mylist, min, max):
    rank = 0
    word = mylist[rank]
    while (WordTester(word) and ForkGrabber(min, max, word)):
        rank += 1
        if rank == len(mylist):
            return rank
        word = mylist[rank]
    return rank


fr = open("Data/exemple.txt", "r", encoding="utf-8")

print(len(fr.read()))

fr.close()

print(ranker("certains économistes étaient en exil dans la forêt\n", 0, 12))

# main
export(20, 5, 100)

print(ranker("sans un sous re toi\n", 0, 100))
