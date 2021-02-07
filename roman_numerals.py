
#function to convert an integer to a roman numeral
def int_to_roman(num):
    #list of roman numerals
    romans = ['I', 'V', 'X', 'L', 'C', 'D', 'CM', 'M']
    ints = [1, 5, 10, 50, 100, 500, 900, 1000]
    result = '' #string that will be the result conversion
    length = len(romans)-1
    i = length
    while num > 0: 
        if num >= ints[i]:
            result += romans[i]
            num = num - ints[i]
        else:
            i = i-1

    return result

  
num = int(input("Enter an integer to convert to a roman numeral. \nEnter -1 to quit: "))
while num != -1:
    print(str(num) + ' converted to a roman numeral is : ' + str(int_to_roman(int(num))))
    num = int(input("Enter an integer to convert to a roman numeral. \nEnter -1 to quit: "))
print('Goodbye.')

        


