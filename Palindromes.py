#Nicholas Feanny; naf16b

originalString = ""
parsedString = ""
palindromes = {}
increment = 1

originalString = input("Please enter the strings:\n")

while originalString != "Done":
    parsedString = originalString.replace(" ", "").lower()

    if parsedString == parsedString[::-1]:
        palindromes[increment] = originalString
        increment += 1

    originalString = input()
print("The palindromes are: {a}".format(a=palindromes))