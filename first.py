# Store the name of 5 peoples
# generate some message with their name. 

names = []
# names = list()

name = "Hello"

for i in range(5): # range(0,5)
    # ... ellipses
    names.append(input(f"Enter {i+1}st name: ").title())

for name in names:
    print(f"Welcome,{name}!")

# print(names[0])

# for(int i = 0; i < 5; i++)
# range(n) -> 0 till n - 1
# range(m, n) -> m till n - 1 m->start n-end
# for(int i = 1; i <= 5; i++)
# range(start,end,step) -> 1 to 6 -> s = 2 -> 1, 3, 5
# for(int i = 1; i <= 5; i += 2)
# for int number : nums{sop(number)}
# for fruit in fruits:
#    print(fruit)

# print(type(...))

