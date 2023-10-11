def changeFromRoman(user_input):
    roman_numerals = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
    int_value = 0

    if(user_input==None):
        return "invalid"
    
    user_input = user_input.upper()

    for i in range(len(user_input)):
        if user_input[i] in roman_numerals:
            if i + 1 < len(user_input) and roman_numerals[user_input[i]] < roman_numerals[user_input[i + 1]]:
                int_value -= roman_numerals[user_input[i]]
            else:
                int_value += roman_numerals[user_input[i]]
        else:
            return "invalid"

    return int_value