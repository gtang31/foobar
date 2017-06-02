def answer(plaintext):
    # your code here
    
    braille_mapping = {
        'A': '100000',
        'B': '110000',
        'C': '100100',
        'D': '100110',
        'E': '100010',
        'F': '110100',
        'G': '110110',
        'H': '110010',
        'I': '010100',
        'J': '010110',
        'K': '101000',
        'L': '111000',
        'M': '101100',
        'N': '101110',
        'O': '101010',
        'P': '111100',
        'Q': '111110',
        'R': '111010',
        'S': '011100',
        'T': '011110',
        'U': '101001',
        'V': '111001',
        'W': '010111',
        'X': '101101',
        'Y': '101111',
        'Z': '101011',
        ' ': '000000'}
    def _special_printer(ch):
        if (ch in braille_mapping) and (ch != ' '):
            # add capitalization mark
            return '000001' + braille_mapping[ch]
        else:
            return braille_mapping[ch.upper()]
    s = ''
    for ch in plaintext:
        s += _special_printer(ch)
    return s
