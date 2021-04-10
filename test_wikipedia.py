import wikipedia

input = raw_input("Q: ")

print(wikipedia.summary(input,sentences=1))