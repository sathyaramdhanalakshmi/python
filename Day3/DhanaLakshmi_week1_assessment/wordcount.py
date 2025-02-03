def cnt_occurances(sentence):
    words=sentence.split()
    cnt={}
    for i in words:
        if i in cnt:
            cnt[i]+=1
        else:
            cnt[i]=1
    return cnt

def main():
    sentence=input("enter th sentence: ")
    wordcnt=cnt_occurances(sentence)
    for word,cnt in wordcnt.items():
        print(f"{word}:{cnt}")
        
main()
    