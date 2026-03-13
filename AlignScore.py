from Bio import Align

gen_A = "ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGC"
gen_B = "CATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGC"

aligner = Align.PairwiseAligner()

aligner.match_score = 1
aligner.mismatch_score = -1 
aligner.open_gap_score = -2

alignments = aligner.align(gen_A, gen_B)
best_alignment = alignments[0]

print("Best Alignment Score:", best_alignment.score)
print(best_alignment)