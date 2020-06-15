from core.methodword import *

# This Program Was Written By Damiisdandy
# github.com/damiisdandy

try:
    print(Colors.CYAN + Colors.BOLD + "TYPE IN ANY INTEGER RANGING FROM 1 - 1,000,000,000 , IT WILL BE CONVERTED TO "
                                      "WORDS"
          + Colors.ENDC)
    while True:
        try:
            number = int(input(Colors.BOLD + ">>> " + Colors.ENDC))
            # numbers already in dictionary

            if number == 0:
                print("Zero")
            elif number in numdict:
                print(numdict.get(number).title())

            # from numbers 21 - 99
            elif 100 > number > 20:
                print(tenseword(number))

            # from numbers 100 - 999
            elif 1000 > number > 99:
                print(hundredword(number))

            # from numbers 1,000 - 9,999
            elif 10000 > number > 999:
                print(thousword(number))

            # 10,000 - 99,999
            elif 100000 > number > 9999:
                print(tenthousword(number))

            # 100,000 - 999,999
            elif 1000000 > number > 99999:
                print(hunthousword(number))

            # 1,000,000 - 99,999,999
            elif 100000000 > number > 999999:
                mil = number // 1000000
                mil_thous = number % 1000000

                if mil_thous == 0:
                    print(f"{tenseword(mil)} Million")
                elif mil_thous in numdict:
                    print(f"{tenseword(mil)} Million And {numdict.get(mil_thous)}")
                elif 100 > mil_thous > 20:
                    print(f"{tenseword(mil)} Million And {tenseword(mil_thous)}")
                elif 1000 > mil_thous > 99:
                    print(f"{tenseword(mil)} Million And {hundredword(mil_thous)}")
                elif 10000 > mil_thous > 999:
                    print(f"{tenseword(mil)} Million {thousword(mil_thous)}")
                elif 100000 > mil_thous > 9999:
                    print(f"{tenseword(mil)} Million {tenthousword(mil_thous)}")
                elif 1000000 > mil_thous > 99999:
                    print(f"{tenseword(mil)} Million {hunthousword(mil_thous)}")

            elif 1000000000 > number > 9999999:
                mil = number // 1000000
                mil_thous = number % 1000000

                if mil_thous == 0:
                    print(f"{hundredword(mil)} Million")
                elif mil_thous in numdict:
                    print(f"{hundredword(mil)} Million And {numdict.get(mil_thous)}")
                elif 100 > mil_thous > 20:
                    print(f"{hundredword(mil)} Million And {tenseword(mil_thous)}")
                elif 1000 > mil_thous > 99:
                    print(f"{hundredword(mil)} Million And {hundredword(mil_thous)}")
                elif 10000 > mil_thous > 999:
                    print(f"{hundredword(mil)} Million {thousword(mil_thous)}")
                elif 100000 > mil_thous > 9999:
                    print(f"{hundredword(mil)} Million {tenthousword(mil_thous)}")
                elif 1000000 > mil_thous > 99999:
                    print(f"{hundredword(mil)} Million {hunthousword(mil_thous)}")

            elif number == 1000000000:
                print('One Billion')

            else:
                print(Colors.YELLOW + "ONLY NUMBERS FROM ZERO TO ONE BILLION!" + Colors.ENDC)
        except ValueError:
            print(Colors.RED + "NUMBERS ONLY!" + Colors.ENDC)
except KeyboardInterrupt:
    print("\n" + Colors.BOLD + Colors.GREEN + "Program Closed Succesfully" + Colors.ENDC)
