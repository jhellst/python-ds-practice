def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    newString = ""
    for index in range(len(phrase) - 1, -1, -1):
        newString += phrase[index]
    return newString
