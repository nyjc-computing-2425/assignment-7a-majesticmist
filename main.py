# Write a function to convert numbers to text numerals

def text_numeral(num):
    """
    
    """
    #create num_word dict
    NUM_WORD = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    #greedy
    if num <= 20:
      return NUM_WORD[num]

    ten = num//10
    one = num%10
    return NUM_WORD[ten*10] + " " + NUM_WORD[one]