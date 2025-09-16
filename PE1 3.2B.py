#Write a program to find nd print all numbers divisible by 7, between 1 and 300, use a for loop and include %.

for i in range(1, 301):
    if i % 7 == 0:
        continue
    print(i)
    
