# word=input("enter a string")

# word2=input("enter a string")

# srt_word=sorted(word)

# srt_word2=sorted(word2)



# print("anagram " if srt_word==srt_word2 else "not anagram")
#*******

word1="supervisor"
word2="superior"

wc={}
is_kangaroo=True
for c in word1:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1

for ch in word2:
    if ch in wc and wc[ch]>0:
        wc[ch]-=1
    else:
        is_kangaroo=False
        break

print(is_kangaroo)
    

