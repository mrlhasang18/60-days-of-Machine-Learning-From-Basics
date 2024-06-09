# Now lets look at the big O notation of the programs

# O(1):It means that the time complexity of an algorithm is constant, i.e., it does not depend on the input size.

car = ['lamborgini','ferari','Tesla']
def choose(car):
    print(car[1])

print("\n--- Big O Notation: O(1) ---- ")
choose(car)

# O(n):  Due to the n operations, if n=2 (2 operations)
# for loop
def choose(car):
    for i in car:
        print(i)

print("\n--- Big O Notation: O(n) ---- ")
choose(car)

# O(n^2):  Due to the n^2 operations, if n=3 (3*3 = 9 operations) 
# nested for loop
def choose(car):
    for i in car:
        for j in car:
            print(i,j)

print("\n--- Big O Notation: O(n^2) ---- ")
choose(car)

