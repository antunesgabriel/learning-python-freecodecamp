def verify_card_number(card_number):
    inverted_card_number = card_number[::-1]

    odd_digits_sum = 0
    even_digits_multiplication = 0

    odd_digits = inverted_card_number[::2]
    even_digits = inverted_card_number[1::2]

    for digit in odd_digits:
        odd_digits_sum += int(digit)

    for digit in even_digits:
        number = int(digit) * 2
        if number > 9:
            print(number)

    print("odd_digits_sum: ", odd_digits_sum)
    print("even_digits_multiplication: ", even_digits_multiplication)


def main():
    card_number = "4111-1111-4555-1142"
    card_translation = str.maketrans({"-": "", " ": ""})
    translated_card_number = card_number.translate(card_translation)

    # print("translated:", translated_card_number)
    # print("reverted:", translated_card_number[-4:])
    # print("all inverted string:", translated_card_number[::-1])
    # print("all even digits position:", translated_card_number[::-1][1::2])

    verify_card_number(translated_card_number)


main()
