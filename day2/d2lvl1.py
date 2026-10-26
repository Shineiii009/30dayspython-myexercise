# Day 2: 30 days og python programming
first_name = "Sydney"
last_name = "Magsanay"
full_name = "Sydney Magsanay"
country = "Philippines"
city = "Quezon City"
age  = 19
year = 1999
is_married = True
is_true = False
is_light_on = False

a,b,c = 1,2,3

print(type(first_name))
print(type(last_name))    # <class 'str'>
print(type(full_name))    # <class 'str'>
print(type(country))      # <class 'str'>
print(type(city))         # <class 'str'>
print(type(age))          # <class 'int'>
print(type(year))         # <class 'int'>
print(type(is_married))   # <class 'bool'>
print(type(is_true))      # <class 'bool'>
print(type(is_light_on))  # <class 'bool'>

print(len(first_name))
print(len(last_name))

num_one = 5
num_two =4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = pow(num_one, num_two)
floor_division = num_one // num_two

print(total, diff, product, division, remainder, exp, floor_division)

PI = 3.14159
radius = int(input("Enter radius: "))
area_of_circle = PI * pow(radius, 2)
circum_of_circle = 2 * PI * radius

print("Area of circle: ",  area_of_circle)
print("Circumference: ",  circum_of_circle)


