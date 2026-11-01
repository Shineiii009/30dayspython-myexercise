language = 'Python'

first_three = language[0:3]
print(first_three)

last_three = language[3:6]
print(last_three)

last_three = language[-3:]
print(last_three)

last_three = language[3:]
print(last_three)

greeting= 'Hello World'
print(greeting[::-1])

pto = language[0:6:2]
print(pto)

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

#find first occurence rfind last occurence

#1
first_word = 'Thirty'
second_word = 'Days'
third_word = "Of"
fourth_word = "Python"

print(f"{first_word} {second_word} {third_word} {fourth_word}")

#2
first_word = 'Coding'
second_word = 'For'
third_word = "All"

print(f"{first_word} {second_word} {third_word} {fourth_word}")

#3 #4 #5 #6 7 8 9 10
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.swapcase())
print(company[1:])
#11
word = "Python for Everyone"
print(word.replace("Everyone", "All"))

#12
print(company.split())

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

#15
print(company[0:1])

print(f"{word[0:1]}{word[7:8]}{word[11:12]}")

print(company.index("C"))
print(company.index("F"))

phrase = "You cannot end a sentence with because because because is a conjunction"
print(phrase.find("because"))
print(phrase.rfind("because"))
print(phrase.rindex("because"))
print(phrase.strip("because"))

print(company.index("Coding"))

newCompany = '   Coding For All      '
print(newCompany.strip())

var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier())
print(var2.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries)
print(result)

print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")