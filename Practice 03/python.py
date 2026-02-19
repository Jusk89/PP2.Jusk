to_digit = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

to_word = {v: k for k, v in to_digit.items()}

def decode(s):
    res = ""
    for i in range(0, len(s), 3):
        res += to_digit[s[i:i+3]]
    return int(res)

def encode(num):
    return "".join(to_word[d] for d in str(num))


s = input()

for op in "+-*":
    if op in s:
        left, right = s.split(op)
        break

a = decode(left)
b = decode(right)

if op == "+":
    ans = a + b
elif op == "-":
    ans = a - b
else:
    ans = a * b

print(encode(ans))