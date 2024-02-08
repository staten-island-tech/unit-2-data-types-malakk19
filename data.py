#integers, booleans, strings
#challange 1
""" x = (int(input("Is it even or odd?")))
if (x%2) > 0:
    print("odd")
else:
    print("even")

##challange 2

x = int(input("What is the bill?"))
service = input("how was the service? ")
if service == "bad":
    print(x)
if service == "okay":
    print(x + (x%15))
if service == "good":
    print(x + (x%20))
if service == "great":
    print(x+ (x%25))

    ##challenge 3 """
def allfactors (n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
            return factors
number = int(input("please enter a number: "))
listfactors = allfactors(number)
print(listfactors)
