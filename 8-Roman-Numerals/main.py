def getNumeralGroups(numerals):
    numeral_groups = []
    for numeral in numerals:
        if len(numeral_groups) == 0:
            numeral_groups.append(numeral)
        elif numeral in numeral_groups[-1]:
            numeral_groups[-1] = numeral_groups[-1] + numeral
        else:
            numeral_groups.append(numeral)
    return numeral_groups
    
def getDecimalGroups(numerals):
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    return list(map(lambda n: mapping[n[0]] * len(n), numerals))
    
def sumDecimalGroups(decimal_groups):
    total = 0
    group_total = 0
    for i in range(len(decimal_groups)):
        if i == 0:
            group_total = decimal_groups[i]
            
        elif decimal_groups[i] < decimal_groups[i - 1]:
            total += group_total
            group_total = decimal_groups[i]
            
        elif decimal_groups[i] > decimal_groups[i - 1]:
            group_total = decimal_groups[i] - group_total
            
        if i == len(decimal_groups) - 1:
            total += group_total
            
    return total

def numeralsToDecimal(numerals):
    numeral_groups = getNumeralGroups(numerals)
    decimal_groups = getDecimalGroups(numeral_groups)
    decimal = sumDecimalGroups(decimal_groups)
    return decimal

def compare(a, b):
    return (numeralsToDecimal(a) < numeralsToDecimal(b))
