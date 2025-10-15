def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word) > 1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)

    print("Lists of words with the same first and last letter\n",lst)
    return ctr

count= match_words(['abc','cfc','xyz','aba','1221'])
print("Count of words with the same first and last letter is:",count)
