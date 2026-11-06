def camel_to_hyphen(text: str) -> str:
    result = []
    for char in text:
        if char.isupper():
            result.append('-')
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)
#############test
print(camel_to_hyphen("helloPython"))