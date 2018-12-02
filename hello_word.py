#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

message = "hello python"
print(message)
print("hello everyone.")
#将首字母大写
print(message.title())
#将字符串全部大写

favorite_language=' python '
favorite_language.rstrip()
print(favorite_language)
print(favorite_language.strip())
print(favorite_language.lstrip()+favorite_language.strip()+ '\n'+favorite_language)

#对数列的增删改查
alist=['apple','pear','egg','bear']
print alist
print(alist[0],alist[1],alist[2],alist[3])
print("so sorry for "+alist[2]+" that can't come here!")
del alist[2]
alist.insert(2,'star')
print alist
alist[2]='car'
print alist
alist.append('moon')
print alist
alist.pop()
print alist
alist.pop()
alist.pop()
alist.pop()
print alist
del alist[0]
print alist

#对数列的排序
blist=['pear','egg','bear','orange','moon']
sorted(blist)
print blist
print(sorted(blist))
print(sorted(blist,reverse=True))
print blist
print(len(blist))

