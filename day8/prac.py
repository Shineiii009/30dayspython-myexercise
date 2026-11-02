# add one item only update multiple items
# remove one item only pop random item clear all item del whole
# union combining sets into new sets T
# update his method inserts a set into a given set
# intersection similar element
# Subset (A ⊆ B): Set A is a subset of set B if every element in A is also in B.
# Superset (A ⊇ B): Set A is a superset of set B if A contains every element found in B.

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['NVidia', 'Anthropic', 'Open AI'])
print(it_companies)
it_companies.remove('Oracle')

#level2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del(A)
del(B)
del(C)

age = [22, 19, 24, 25, 26, 24, 25, 24]
new_age = set(age)
print(len(age))
print(len(new_age))

word = "I am a teacher and I love to inspire and teach people."
print(word.split())
new_word = set(word.split())
print(f"The amount of unique words is: {len(new_word)}")