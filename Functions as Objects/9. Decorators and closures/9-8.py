# a higher-order function to calculate a running average


def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


# Test 
avg = make_averager()
print(
    avg(10),
    avg(11),
    avg(20),
     )