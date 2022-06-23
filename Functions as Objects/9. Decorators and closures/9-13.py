# Calculate a running average without keeping all history (fixed with the use of nonlocal)

def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager

    # Test 
avg = make_averager()
print(
    avg(10),
    avg(11),
    avg(20),
     )