matrix_string = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

# Split the matrix string into rows
rows = matrix_string.split('\n')

# Initialize an empty list to store characters from each column
columns = [''] * len(rows[0])

# Traverse each row and concatenate characters into columns
for row in rows:
    for i, char in enumerate(row):
        columns[i] += char

# Concatenate characters from each column to reveal the hidden message
hidden_message = ''.join(columns)

print("Hidden Message:", hidden_message)
