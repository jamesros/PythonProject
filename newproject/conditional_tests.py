car = 'subaru'
print("Is car == 'subaru' ? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi' ? I predict false")
print(car == 'audi')

cars = ['bmw', 'audi', 'toyota', 'subaru', 'nissan', 'honda']
for car in cars:
    if car == 'honda' or car == 'nissan':
        print("That " + car + " is a great car!")
    else:
        print("I do not really like " + car + " cars.")
