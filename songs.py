def count_substitutions(s):
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    consonants = {'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш',
                  'щ', 'ь', 'ъ'}

    count = 0
    last_char_type = None

    for c in s:
        if c.lower() in vowels:
            char_type = 'vowel'
        elif c.lower() in consonants:
            char_type = 'consonant'
        else:
            continue

        if last_char_type is None:
            last_char_type = char_type
            continue

        if last_char_type == char_type:
            count += 1
            if char_type == "consonant":
                char_type = "vowel"
            else:
                char_type = "consonant"

        last_char_type = char_type

    return count

s = input().replace(" ", '')
print(min(count_substitutions(s), count_substitutions(s[::-1])))