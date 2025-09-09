count = 0
def print_numbers():
    global count
    if(count == 3):
        return
    print(count)
    count += 1
    print_numbers()
print_numbers()