import argparse
import math
import collections
import euler

def number_to_words(number):
    dictionary = { 0 : '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six',
                7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'eleven', 12 : 'twelve',
               13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen',
               18 : 'eighteen', 19 : 'nineteen', 20 : 'twenty', 30 : 'thirty', 40 : 'forty',
               50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
    words = ''
    #21124

    thousands = number/1000
    hundreds  = (number%1000)/100
    if number % 100 < 20 and number % 100 > 10:
        teens = number % 100
        units = 0
    else:
        teens = ((number%100)/10)*10
        units = (number%10)

    if thousands != 0:
        words += dictionary[thousands] + ' thousand'
    if hundreds != 0:
        if words != '': words += ' and '
        words += dictionary[hundreds] + ' hundred'
    if teens != 0:
        if words != '': words += ' and '
        words += dictionary[teens]
    if units != 0:
        if words != '':
            if teens == 0:
                words += ' and '
            else:
                words += ' '
        words += dictionary[units]

    return words

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 17 of Euler Project')
    parser.add_argument('--limit', type=int, default=5)
    args = parser.parse_args()

    length = 0
    for i in xrange(1, args.limit+1):
        length += len(number_to_words(i).replace(' ', ''))

    print length
