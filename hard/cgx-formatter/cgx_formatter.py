n = int(input())

result = inten = prev = ''

# get raw input and squash it into single line
raw_text = ''.join([input().strip() for _ in range(n)])

# bool, if current char is in key value
is_key_val = False

# loop over all chars in raw_text and parse it
for char in raw_text:
    if char == '\'':
        is_key_val = not is_key_val
        result += char
    elif is_key_val:
        result += char
    elif char == ' ' or char == '\t':
        continue
    elif char == '(':
        if prev == '=':
            result += '\n' + inten
        result += char + '\n'
        inten += '    '
        result += inten
    elif char == ')':
        inten = inten[:-4]
        if prev == '(':
            result = result[:-4]
            result += ')'
        else:
            result += '\n' + inten + char
    elif char == ';':
        result += char + '\n' + inten
    else:
        result += char
    prev = char

print(result)
