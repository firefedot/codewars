def remove_exclamation_marks(s):
    arrey = ''
    for i in range(0, len(s)):
        if s[i] != '!':
            arrey += s[i]
    return arrey
    # return s.replace('!', '')


print(remove_exclamation_marks('Ge!'))

