dictionary = {
    "Zhusup": 95,
    "Adiat": 89,
    "Asan": 90
}

for name, x in dictionary.items():
    if 0 <= x < 50:
        gpa = "FX"
    elif 50 < x < 70:
        gpa = "2"
    elif 70 < x < 75:
        gpa = "2.33"
    elif 75 < x < 80:
        gpa = "2.67"
    elif 80 < x < 85:
        gpa = "3"
    elif 85 < x < 90:
        gpa = "3.33"
    elif 90 < x < 95:
        gpa = "3.67"
    else:
        gpa = "4"

    print(f"{name}: {gpa}")
