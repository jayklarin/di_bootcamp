MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM#
$a
#t%'''


def print_matrix(matrix):
    """Helper to print the 2D matrix in a readable grid form."""
    for row in matrix:
        print(row)


def decode_matrix(matrix_str: str) -> str:
    """
    Decode the hidden message by:
    1. Converting the string into a 2D matrix (list of lists).
    2. Reading column by column (c), each row (r).
    3. Collapsing symbol runs into a single space (between letters).
    """
    # ---- Step 1: Build 2D matrix ----
    rows = matrix_str.strip('\n').split('\n')
    num_rows = len(rows)
    num_cols = max(len(row) for row in rows)

    # Pad rows with spaces so all are the same length
    matrix = [[rows[r][c] if c < len(rows[r]) else ' ' for c in range(num_cols)]
              for r in range(num_rows)]

    # Print matrix for visualization
    print("2D Matrix representation:")
    print_matrix(matrix)
    print()  # blank line for spacing

    # ---- Step 2: Read column by column ----
    col_text_chars = []
    for c in range(num_cols):       # columns
        for r in range(num_rows):   # rows (top to bottom)
            col_text_chars.append(matrix[r][c])
    col_text = ''.join(col_text_chars)

    # ---- Step 3 & 4: Filter/clean ----
    result = []
    r = 0
    n = len(col_text)

    while r < n:
        ch = col_text[r]

        if ch.isalpha():
            result.append(ch)
            r += 1
        else:
            c = r
            while c < n and not col_text[c].isalpha():
                c += 1

            prev_is_letter = bool(result) and result[-1].isalpha()
            next_is_letter = (c < n) and col_text[c].isalpha()

            if prev_is_letter and next_is_letter:
                result.append(' ')

            r = c

    return ''.join(result).strip()


# ---- Step 5: Decode and print ----
decoded_message = decode_matrix(MATRIX_STR)
print("Decoded Message:", decoded_message)
