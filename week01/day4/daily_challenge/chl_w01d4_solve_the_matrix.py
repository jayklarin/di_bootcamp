MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM#
$a
#t%'''


def decode_matrix(matrix_str: str) -> str:
    """
    Decode the hidden message by:
    1. Converting the string into a 2D matrix (list of lists).
    2. Reading column by column (c), each row (r).
    3. Collapsing symbol runs into a single space (between letters).
    """
    # ---- Step 1: Build 2D matrix ----
    rows = matrix_str.strip('\n').split('\n')
    max_len = max(len(row) for row in rows)

    # Pad rows with spaces so all are same length
    matrix = [[row[c] if c < len(row) else ' ' for c in range(max_len)] for row in rows]

    # ---- Step 2: Read column by column ----
    col_text_chars = []
    for c in range(max_len):          # loop over columns
        for r in range(len(matrix)):  # loop down each row
            col_text_chars.append(matrix[r][c])
    col_text = ''.join(col_text_chars)

    # ---- Step 3 & 4: Keep letters, collapse symbol runs ----
    result = []
    r = 0
    n = len(col_text)

    while r < n:
        ch = col_text[r]
        if ch.isalpha():
            result.append(ch)
            r += 1
        else:
            # consume run of non-letters
            c = r
            while c < n and not col_text[c].isalpha():
                c += 1

            prev_is_letter = result and result[-1].isalpha()
            next_is_letter = (c < n) and col_text[c].isalpha()

            if prev_is_letter and next_is_letter:
                result.append(' ')
            r = c

    return ''.join(result).strip()


# ---- Step 5: Decode and print ----
decoded_message = decode_matrix(MATRIX_STR)
print(decoded_message)
