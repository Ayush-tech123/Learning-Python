marks = [43,45,54,54,32,56,87,54,98,78]
print(marks)
print(marks[6])
print(marks[-1])
print(marks[3:])
print(marks[5:7])

marks[1] = 99
print(marks[1])

marks.extend("pass")
print(marks)

marks.remove("p")
print(marks)
marks.remove("a")
print(marks)
marks.remove("s")
print(marks)
marks.remove("s")
print(marks)

marks.append("fail")
print(marks)

marks.insert(2,0)
print(marks)

marks.remove(99)
print(marks)

marks.pop()
print(marks)

print(marks.index(98))
print(marks.count(54))

mark = marks.copy()
print(mark)

marks.sort()
print(marks)

marks.clear()
print(marks)




