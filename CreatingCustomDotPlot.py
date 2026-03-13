import numpy as np
import matplotlib.pyplot as plt

sequence_1 = "ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGC"
sequence_2 = "CTCGATCGATCGAGACTAGCTAGCTATCTCGAG"

dot_matrix = np.zeros((len(sequence_1), len(sequence_2)))   

for i,char1 in enumerate(sequence_1):
    for j,char2 in enumerate(sequence_2):
        if char1 == char2:
            dot_matrix[i][j] = 1

plt.imshow(dot_matrix, cmap='Greys', interpolation='nearest')
plt.title('Dot Plot of Sequence Alignment')
plt.xlabel('Sequence 2')
plt.ylabel('Sequence 1')
plt.xticks(range(len(sequence_2)), list(sequence_2))
plt.yticks(range(len(sequence_1)), list(sequence_1))
plt.show()