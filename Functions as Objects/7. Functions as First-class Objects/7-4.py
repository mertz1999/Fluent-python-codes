# Example 7-4. Sorting a list of words by their reversed spelling


def reverse(word):
    return word[::-1]

print(reverse('testing'))


fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=reverse))
