# # for i in range(1,11):
# #     print(i)
# test=input('enter the secret word')
# ss=''
# for t in test:
#     ss +=chr(ord(t)-1)
# print(ss)
secret=input('enter your secret number')
test=''
for s in secret:
    test +=chr(ord(s)+1)
print(test)