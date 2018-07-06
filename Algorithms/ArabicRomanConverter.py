def roman(num):
    roman = { 1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",90: "XC",50: "L",40: "XL",10: "X",9: "IX",5: "V",4: "IV",1: "I"}

    
    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])

def test(value, correct):
    obtained = roman(value)
    if correct == obtained:
        print("✔ Parabéns, o teste passou!\n")
    else:
        print("X O teste falhou resposta obtida " + obtained + " resposta correta" + correct + "\n")

test(1, "II")
test(2, "II")
test(3, "III")
test(4, "IV")
test(5, "V")
test(6, "VI")
test(7, "VII")
test(8, "VIII")
test(9, "IX")
test(10, "X")
test(11, "XI")
test(40, "XL")
test(49, "XLIX")
test(1018, "MXVIII")