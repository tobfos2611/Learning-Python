txt = "TeXt\n\"TeXt\""
#      0123 4 56789

print("TeXt\n\"TeXt\"")
print("\\TeXt\\")
print(txt + " is text")
print("duh")
print(txt.lower())
print(txt.upper())
print(txt.isupper())
print(txt.islower())
print(txt.upper().isupper())
print(len(txt + " Hello!"))
print(txt[0])
print(txt[1])
print(txt[2])
print(txt[3])
print(txt[0] + txt[1] + txt[2] + txt[3])
print(txt.index("T"))
print(txt.index("e"))
print(+txt.index("X"))
print(txt.index("t"))
print(txt.index("\n"))
print(txt.index("\""))
print(txt.replace("TeXt", "tExT") + (txt.replace ("\"", "'")))
