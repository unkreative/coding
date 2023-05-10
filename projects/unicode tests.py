test = "h "

utf8string = test.encode("utf-8")
asciistring = test.encode("ascii")
isostring = test.encode("ISO-8859-1")
utf16string = test.encode("utf-16")
print(test)

print(utf8string)
print(asciistring)
print(isostring)
print(utf16string)
print()


print(type(utf16string))

print(utf16string.decode("utf-16"))