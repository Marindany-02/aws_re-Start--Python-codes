# Read the clean preproinsulin sequence from the file
with open('preproinsulin-seq-clean.txt', 'r') as file:
    sequence = file.read().strip()  # Strip any accidental leading/trailing whitespace

# Extract and save the sequences directly

# Signal sequence (1-24)
with open('lsinsulin-seq-clean.txt', 'w') as file:
    file.write(sequence[:24])

# B chain (25-54)
with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(sequence[24:54])

# C peptide (55-89)
with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(sequence[54:89])

# A chain (90-110)
with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(sequence[89:110])