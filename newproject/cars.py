cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the unsorted list:")
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print(len(cars))
