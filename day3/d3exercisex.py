age = 19
height = 169.3
imaginary = 4j

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

perimeter = a + b + c

print("The perimeter of the triangle is ", perimeter)

m = 2
b = -2

slope = m
y = b
x = -b/m

point_1 = (2,2)
point_2 = (6,10)

pointSlope = (point_2[1] - point_1[1]) / (point_2[0] - point_1[1])

print("First slope: ", slope, "Second slope: ", pointSlope)

#11
x = 0
y = pow(x, 2) + 6 * x + 9

print(y)
#12
print(len('python') > len('dragon'))

print('on' in 'python' and 'dragon')

print('jargon' in 'I hope this course is not full of jargon.')

print('on' not in 'python' and 'dragon')

size = len('python')
print(float(size))

x % 2 ==0

value = 2.7

print(7 // 3 == value)

print(type('10') == type(10))

print(int(9.8) == 10)

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
weekly_earning = hours * rate

print("Your weekly earnis is ", weekly_earning)

years = int(input("Enter number of years you have lived: "))
convert_seconds = years * 365 * 24 * 60 * 60
print("You have lived for ", convert_seconds, "seconds")

# Loop from 1 to 5 to generate each row
for i in range(1, 6):
    
    col1 = i
    col2 = 1
    col3 = i
    col4 = i ** 2
    col5 = i ** 3
    print(f"{col1} {col2} {col3} {col4} {col5}")

