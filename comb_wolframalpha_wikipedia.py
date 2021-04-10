import wikipedia
import wolframalpha

app_id = "H4K399-TUE2PT76GV"
client = wolframalpha.Client(app_id)

while True:
    input = raw_input("Q: ")

    try:
        # Wolfralpha API
        res = client.query(input)
        answer = next(res.results).text
        print(answer)
    except:
        # Wikipedia API
        print(wikipedia.summary(input,sentences=2))