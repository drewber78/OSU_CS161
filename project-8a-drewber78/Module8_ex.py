eng_to_span = {
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "quatro",
    "five": "cinco",
    "six": "seis",
    "seven": "siete",
    "eight": "ocho",
    "nine": "nueve",
    "ten": "diez"
}

for index in eng_to_span:
    print(index, eng_to_span[index])

def some_squares(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i * i

    return d