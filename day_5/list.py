# append end insert specific remove pop del using index range

names = ["Sydney", "Rc", "Kylle", "Ian", "James"]

print(len(names))
mixed_data_types = ["Sydney", 13, 167.8, "Single", "Philippines"]

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[-4])
print(it_companies[-6])
print( it_companies[-1])

it_companies.append("Amazon")
print(it_companies)

it_companies.insert(5, "Nvidia")
print(it_companies)

print(it_companies[3].upper())

hash ="# ".join(it_companies)
print(hash)

print("Alibaba" in it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[3:])
del(it_companies)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
full_stack.insert(5, "Python")
full_stack.insert(5, "SQL")
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))

for age in ages:
    average = 0
    average+=age

print(average / len(ages))

print(f"Range: {max(ages) - min(ages)}" )
value1 = min(ages) - average
value2 = max(ages) -average
print(abs(value1+value2))

