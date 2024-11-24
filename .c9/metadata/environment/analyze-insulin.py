{"changed":true,"filter":false,"title":"analyze-insulin.py","tooltip":"/analyze-insulin.py","value":"# Read the clean preproinsulin sequence from the file\nwith open('preproinsulin-seq-clean.txt', 'r') as file:\n    sequence = file.read().strip()  # Strip any accidental leading/trailing whitespace\n\n# Extract and save the sequences directly\n\n# Signal sequence (1-24)\nwith open('lsinsulin-seq-clean.txt', 'w') as file:\n    file.write(sequence[:24])\n\n# B chain (25-54)\nwith open('binsulin-seq-clean.txt', 'w') as file:\n    file.write(sequence[24:54])\n\n# C peptide (55-89)\nwith open('cinsulin-seq-clean.txt', 'w') as file:\n    file.write(sequence[54:89])\n\n# A chain (90-110)\nwith open('ainsulin-seq-clean.txt', 'w') as file:\n    file.write(sequence[89:110])","undoManager":{"mark":9,"position":9,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["\"\"\"","Your module description","\"\"\"",""],"id":10}],[{"start":{"row":0,"column":0},"end":{"row":42,"column":0},"action":"insert","lines":["import re","","# Step 1: Read the preproinsulin sequence from file","with open('preproinsulin-seq.txt', 'r') as file:","    sequence_data = file.read()","","# Step 2: Clean the sequence by removing metadata (ORIGIN, numbers, spaces, line breaks, slashes)","clean_sequence = re.sub(r'[^a-zA-Z]', '', sequence_data)  # Remove non-alphabetic characters","print(\"Cleaned Sequence:\", clean_sequence)","","# Step 3: Extract different parts of the insulin sequence","","# Signal sequence (amino acids 1-24)","lsinsulin_seq = clean_sequence[:24]","with open('lsinsulin-seq-clean.txt', 'w') as file:","    file.write(lsinsulin_seq)","print(\"Signal sequence (1-24):\", lsinsulin_seq)","","# B chain (amino acids 25-54)","binsulin_seq = clean_sequence[24:54]","with open('binsulin-seq-clean.txt', 'w') as file:","    file.write(binsulin_seq)","print(\"B chain (25-54):\", binsulin_seq)","","# C peptide (amino acids 55-89)","cinsulin_seq = clean_sequence[54:89]","with open('cinsulin-seq-clean.txt', 'w') as file:","    file.write(cinsulin_seq)","print(\"C peptide (55-89):\", cinsulin_seq)","","# A chain (amino acids 90-110)","ainsulin_seq = clean_sequence[89:110]","with open('ainsulin-seq-clean.txt', 'w') as file:","    file.write(ainsulin_seq)","print(\"A chain (90-110):\", ainsulin_seq)","","# Step 4: Verify sequence lengths","print(\"\\nVerification:\")","print(f\"Length of signal sequence: {len(lsinsulin_seq)} (expected 24)\")","print(f\"Length of B chain: {len(binsulin_seq)} (expected 30)\")","print(f\"Length of C peptide: {len(cinsulin_seq)} (expected 35)\")","print(f\"Length of A chain: {len(ainsulin_seq)} (expected 21)\")",""],"id":11}],[{"start":{"row":0,"column":0},"end":{"row":42,"column":0},"action":"remove","lines":["import re","","# Step 1: Read the preproinsulin sequence from file","with open('preproinsulin-seq.txt', 'r') as file:","    sequence_data = file.read()","","# Step 2: Clean the sequence by removing metadata (ORIGIN, numbers, spaces, line breaks, slashes)","clean_sequence = re.sub(r'[^a-zA-Z]', '', sequence_data)  # Remove non-alphabetic characters","print(\"Cleaned Sequence:\", clean_sequence)","","# Step 3: Extract different parts of the insulin sequence","","# Signal sequence (amino acids 1-24)","lsinsulin_seq = clean_sequence[:24]","with open('lsinsulin-seq-clean.txt', 'w') as file:","    file.write(lsinsulin_seq)","print(\"Signal sequence (1-24):\", lsinsulin_seq)","","# B chain (amino acids 25-54)","binsulin_seq = clean_sequence[24:54]","with open('binsulin-seq-clean.txt', 'w') as file:","    file.write(binsulin_seq)","print(\"B chain (25-54):\", binsulin_seq)","","# C peptide (amino acids 55-89)","cinsulin_seq = clean_sequence[54:89]","with open('cinsulin-seq-clean.txt', 'w') as file:","    file.write(cinsulin_seq)","print(\"C peptide (55-89):\", cinsulin_seq)","","# A chain (amino acids 90-110)","ainsulin_seq = clean_sequence[89:110]","with open('ainsulin-seq-clean.txt', 'w') as file:","    file.write(ainsulin_seq)","print(\"A chain (90-110):\", ainsulin_seq)","","# Step 4: Verify sequence lengths","print(\"\\nVerification:\")","print(f\"Length of signal sequence: {len(lsinsulin_seq)} (expected 24)\")","print(f\"Length of B chain: {len(binsulin_seq)} (expected 30)\")","print(f\"Length of C peptide: {len(cinsulin_seq)} (expected 35)\")","print(f\"Length of A chain: {len(ainsulin_seq)} (expected 21)\")",""],"id":12},{"start":{"row":0,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["# Step 1: Read the clean preproinsulin sequence from the file","with open('preproinsulin-seq.txt', 'r') as file:","    clean_sequence = file.read().strip()  # Strip any accidental leading/trailing whitespace","","# Step 2: Extract different parts of the insulin sequence","","# Signal sequence (amino acids 1-24)","lsinsulin_seq = clean_sequence[:24]","with open('lsinsulin-seq-clean.txt', 'w') as file:","    file.write(lsinsulin_seq)","print(\"Signal sequence (1-24):\", lsinsulin_seq)","","# B chain (amino acids 25-54)","binsulin_seq = clean_sequence[24:54]","with open('binsulin-seq-clean.txt', 'w') as file:","    file.write(binsulin_seq)","print(\"B chain (25-54):\", binsulin_seq)","","# C peptide (amino acids 55-89)","cinsulin_seq = clean_sequence[54:89]","with open('cinsulin-seq-clean.txt', 'w') as file:","    file.write(cinsulin_seq)","print(\"C peptide (55-89):\", cinsulin_seq)","","# A chain (amino acids 90-110)","ainsulin_seq = clean_sequence[89:110]","with open('ainsulin-seq-clean.txt', 'w') as file:","    file.write(ainsulin_seq)","print(\"A chain (90-110):\", ainsulin_seq)","","# Step 3: Verify sequence lengths","print(\"\\nVerification:\")","print(f\"Length of signal sequence: {len(lsinsulin_seq)} (expected 24)\")","print(f\"Length of B chain: {len(binsulin_seq)} (expected 30)\")","print(f\"Length of C peptide: {len(cinsulin_seq)} (expected 35)\")","print(f\"Length of A chain: {len(ainsulin_seq)} (expected 21)\")",""]}],[{"start":{"row":34,"column":1},"end":{"row":36,"column":0},"action":"remove","lines":["rint(f\"Length of C peptide: {len(cinsulin_seq)} (expected 35)\")","print(f\"Length of A chain: {len(ainsulin_seq)} (expected 21)\")",""],"id":13}],[{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["-"],"id":14},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":["c"]},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"insert","lines":["l"]},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["e"]},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":["a"]},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["n"]}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":1},"action":"remove","lines":["p"],"id":15},{"start":{"row":33,"column":62},"end":{"row":34,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":14,"column":49},"action":"remove","lines":["# Step 1: Read the clean preproinsulin sequence from the file","with open('preproinsulin-seq-clean.txt', 'r') as file:","    clean_sequence = file.read().strip()  # Strip any accidental leading/trailing whitespace","","# Step 2: Extract different parts of the insulin sequence","","# Signal sequence (amino acids 1-24)","lsinsulin_seq = clean_sequence[:24]","with open('lsinsulin-seq-clean.txt', 'w') as file:","    file.write(lsinsulin_seq)","print(\"Signal sequence (1-24):\", lsinsulin_seq)","","# B chain (amino acids 25-54)","binsulin_seq = clean_sequence[24:54]","with open('binsulin-seq-clean.txt', 'w') as file:"],"id":16}],[{"start":{"row":0,"column":0},"end":{"row":13,"column":28},"action":"remove","lines":["","    file.write(binsulin_seq)","print(\"B chain (25-54):\", binsulin_seq)","","# C peptide (amino acids 55-89)","cinsulin_seq = clean_sequence[54:89]","with open('cinsulin-seq-clean.txt', 'w') as file:","    file.write(cinsulin_seq)","print(\"C peptide (55-89):\", cinsulin_seq)","","# A chain (amino acids 90-110)","ainsulin_seq = clean_sequence[89:110]","with open('ainsulin-seq-clean.txt', 'w') as file:","    file.write(ainsulin_seq)"],"id":17}],[{"start":{"row":1,"column":0},"end":{"row":6,"column":62},"action":"remove","lines":["print(\"A chain (90-110):\", ainsulin_seq)","","# Step 3: Verify sequence lengths","print(\"\\nVerification:\")","print(f\"Length of signal sequence: {len(lsinsulin_seq)} (expected 24)\")","print(f\"Length of B chain: {len(binsulin_seq)} (expected 30)\")"],"id":18},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":20,"column":32},"action":"insert","lines":["# Read the clean preproinsulin sequence from the file","with open('preproinsulin-seq.txt', 'r') as file:","    sequence = file.read().strip()  # Strip any accidental leading/trailing whitespace","","# Extract and save the sequences directly","","# Signal sequence (1-24)","with open('lsinsulin-seq-clean.txt', 'w') as file:","    file.write(sequence[:24])","","# B chain (25-54)","with open('binsulin-seq-clean.txt', 'w') as file:","    file.write(sequence[24:54])","","# C peptide (55-89)","with open('cinsulin-seq-clean.txt', 'w') as file:","    file.write(sequence[54:89])","","# A chain (90-110)","with open('ainsulin-seq-clean.txt', 'w') as file:","    file.write(sequence[89:110])"]}],[{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["-"],"id":19},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":["c"]},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"insert","lines":["l"]},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["e"]},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":["a"]},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["n"]}],[{"start":{"row":0,"column":0},"end":{"row":20,"column":32},"action":"remove","lines":["# Read the clean preproinsulin sequence from the file","with open('preproinsulin-seq-clean.txt', 'r') as file:","    sequence = file.read().strip()  # Strip any accidental leading/trailing whitespace","","# Extract and save the sequences directly","","# Signal sequence (1-24)","with open('lsinsulin-seq-clean.txt', 'w') as file:","    file.write(sequence[:24])","","# B chain (25-54)","with open('binsulin-seq-clean.txt', 'w') as file:","    file.write(sequence[24:54])","","# C peptide (55-89)","with open('cinsulin-seq-clean.txt', 'w') as file:","    file.write(sequence[54:89])","","# A chain (90-110)","with open('ainsulin-seq-clean.txt', 'w') as file:","    file.write(sequence[89:110])"],"id":20}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":32},"end":{"row":20,"column":32},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1729376188706}