# Method 1

my_string = 'Hello, World!'
answer = []
for i in my_string:
    answer.insert(0, i) 

print("".join(answer))
