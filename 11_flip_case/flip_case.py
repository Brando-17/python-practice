def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lower = to_swap.lower()
    output = ''

    for letter in phrase:
        if letter.lower() == lower:
            letter = letter.swapcase()
        output += letter
    return output
print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'h'))