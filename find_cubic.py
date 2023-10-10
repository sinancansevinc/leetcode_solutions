def find_cubic_numbers(num):
    total = 0
    for c in str(num):
        total += int(c)
    
    return (total * total * total) == num
        
    

print(find_cubic_numbers(512))