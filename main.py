## Write a python funtion which will take user input as a number and 
## Will print the table of that number.

# git add .
# git commit -m "msg"
# git push origin main

def generate_table(number):
    for i in range(1,11):
        print(f"{number} * {i} = {number * i}")

generate_table(10)


