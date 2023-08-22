# word="heLLo world"

#capitalize
# print(word.capitalize())
#to capitalize frst word

# print(word.casefold())
#to make it lower case

# print(word.count("L"))
# #to count

#split
# print(word.split(" "))

#find
#specified words index will be shown

word="hit"
# print(word.find("h"))

#startswith
#will return a boolean value
# print(word.startswith("hi"))

# print(word.endswith("t"))

#isalpha()
# print(word.isalpha())

#isdigit()
# print(word.isdigit())

#isalnum()
# word="hi123"
# print(word.isalnum())

# text="one 100 and fifty 5"

# words=text.split(" ")
# for w in words:
#     if w.isdigit():
#         print(w)

#lst comp=>

# text="England promised to continue its aggressiv3 approach to test cricket"
#print the words starting with vowel

# vowels=("a","e","i","o","u")
# words=text.split()
# for w in words:
#     if w[0].casefold() in vowels:
#         print(w)

# ws=[w for w in text.split(" ") if w[0].casefold() in vowels]
# print(ws)

# text="hello i am here in kakkanad"
# #print longest word
# words=text.split(" ")
# print(max(words,key=lambda w:len(w)))







