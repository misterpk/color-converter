def convert_decimal_to_hex(decimal):
    value_list = []
    hex_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
                8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E",
                15: "F"}
    value = ""

    if decimal == 0:
        value = "00"

    while decimal != 0:
        value_list.append(decimal % 16)
        decimal = decimal // 16

    while len(value_list) != 0:
        hex_val = value_list.pop()
        value = value + hex_dict[hex_val]

    if len(value) < 2:
        value = "0" + value

    return value


def convert_to_hex_string(red, green, blue):
    hex_string = "#{}{}{}".format(convert_decimal_to_hex(red),
                                  convert_decimal_to_hex(green),
                                  convert_decimal_to_hex(blue))
    return hex_string


def get_rgb_values_as_dict():
    red_dec = input("Enter the decimal value for red: ")
    green_dec = input("Enter the decimal value for green: ")
    blue_dec = input("Enter the decimal value for blue: ")

    return {"red": int(red_dec),
            "green": int(green_dec),
            "blue": int(blue_dec)}


if __name__ == '__main__':
    '''
    
    *This is the easiest way to do it, using python format conversion*
    
    red_dec = input("Enter the decimal value for red: ")
    green_dec = input("Enter the decimal value for green: ")
    blue_dec = input("Enter the decimal value for blue: ")

    hex_value = "#{:02X}{:02X}{:02X}".format(int(red_dec),
                                             int(green_dec),
                                             int(blue_dec))

    print("The hex color value of ({}, {}, {}) is {}".format(red_dec,
                                                             green_dec,
                                                             blue_dec,
                                                             hex_value))
    '''
    rgb_dict = get_rgb_values_as_dict()

    hex_value = convert_to_hex_string(rgb_dict["red"],
                                      rgb_dict["green"],
                                      rgb_dict["blue"])

    message = "The hex color value of ({0[red]}, {0[green]}, {0[blue]})" \
              " is {1}".format(rgb_dict, hex_value)

    print(message)
