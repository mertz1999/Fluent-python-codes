# Example 7-9. tag generates HTML elements;


def tag(name, *content, class_=None, **attrs):
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs['class'] = class_

    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>'
        for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'


# Test and Results
print(tag('br'), '\n')
print(tag('p', 'hello'), '\n')
print(tag('p', 'hello', 'world'), '\n')
print(tag('p', 'hello', id=33), '\n')
print(tag('p', 'hello', 'world', class_='sidebar'), '\n')
print(tag(content='testing', name="img"), '\n')


