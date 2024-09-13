def digits_to_english(digit):
    digit_map={
        '0':'zero',
        '1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5':'five',
        '6':'six',
        '7':'seven',
        '8':'eight',
        '9':'nine'
    }
    return digit_map.get(digit," ")
def numbers_to_english_text(number):
    no_str=str(number)
    english_text=[digits_to_english(digit) for digit in no_str]
    return " ".join(english_text)
number=int(input("enter the number:"))
english_text=numbers_to_english_text(number)
print(english_text)