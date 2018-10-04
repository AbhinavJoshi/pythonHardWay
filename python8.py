formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("a", "b", "c", "d")
print formatter % (1,"d","d",3)
print formatter % (formatter, formatter,formatter,formatter )