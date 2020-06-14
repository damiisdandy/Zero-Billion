
numdict = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
    80: 'eighty', 90: 'ninty', 100: 'hundred', 200: 'two hundred', 300: 'three hundred', 400: 'four hundred',
    500: 'five hundred', 600: 'six hundred', 700: 'seven hundred', 800: 'eight hundred', 900: 'nine hundred'
}


def tenseword(num):
    unit = num % 10
    tens = (num // 10) * 10

    if num in numdict:
        output = f"{numdict.get(num).title()}"
    else:
        output = f"{numdict.get(tens).title()} {numdict.get(unit).title()}"
    return output


def hundredword(num):
    tens = num % 100
    hund = num // 100

    if num in numdict:
        output = f"{numdict.get(num).title()}"
    elif num < 100:
        output = f"And {tenseword(num)}"
    elif tens in numdict:
        output = f"{numdict.get(hund).title()} Hundred And {numdict.get(tens).title()}"
    elif tens == 0:
        output = f"{numdict.get(hund).title()} Hundred"
    else:
        output = f"{numdict.get(hund).title()} Hundred And " + tenseword(tens)
    return output


def thousword(num):
    hund = num % 1000  # 5, 2, 3 => 523
    thous = num // 1000
    if hund == 0:
        output = f"{numdict.get(thous).title()} Thousand"
    elif hund in numdict:
        output = f"{numdict.get(thous).title()} Thousand And " + f"{numdict.get(hund).title()}"
    elif hund < 100:
        output = f"{numdict.get(thous).title()} Thousand And " + f"{tenseword(hund).title()}"
    else:
        output = f"{numdict.get(thous).title()} Thousand " + f"{hundredword(hund)}"
    return output


def tenthousword(num):
    psudo_tens = num // 1000
    psudo_hund = num % 1000
    if psudo_hund == 0:
        output = f"{tenseword(psudo_tens)} Thousand"
    else:
        output = f"{tenseword(psudo_tens)} Thousand {hundredword(psudo_hund)}"
    return output


def hunthousword(num):
    psudo_hund_thous = num // 1000
    psudo_hund_tens = num % 1000
    if psudo_hund_tens == 0:
        output = f"{hundredword(psudo_hund_thous)} Thousand"
    else:
        output = f"{hundredword(psudo_hund_thous)} Thousand {hundredword(psudo_hund_tens)}"
    return output


# Color Schema
class Colors:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    UNDERLINE = "\033[4m"
    BOLD = "\033[1m"
    ENDC = "\033[0m"