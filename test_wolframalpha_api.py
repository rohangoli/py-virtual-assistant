import wolframalpha

input=raw_input("Question: ")
app_id = "H4K399-TUE2PT76GV"

client = wolframalpha.Client(app_id)

res = client.query(input)
print(res)
print("=================")
# print(res.results)
answer = next(res.results).text

print(answer)
