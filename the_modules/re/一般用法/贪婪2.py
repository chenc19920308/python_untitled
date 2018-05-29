import re
m = re.search("(book)+","mebookbookme")
print(m.group())      # bookbook
print(m.groups())     # ('book',)
a = re.findall("(book)+","mebookbookme")
print(a)              # ['book']
n = re.search("((?:book)+)","mebookbookme")
print(n.group())     #  bookbook
print(n.groups())    # ('bookbook',)
b = re.findall("((?:book)+)","mebookbookme")
print(b)             # ['bookbook']
h = re.search("(book+)","mebookbookme")
print(h.group())    # book
print(h.groups())   #  ('book',)
g = re.findall("(book+)","mebookbookme")
print(g)           # ['book', 'book']