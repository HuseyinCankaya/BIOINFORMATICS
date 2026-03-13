from Bio import SeqIO

# Genome okuma ve Anatasyonları inceleme.

genome_file = "genome.fasta"

for record in SeqIO.parse(genome_file, "fasta"):
    print(f"ID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Sequence Length: {len(record.seq)}")
    print(f"Sequence: {record.seq[:50]}...")  # Print the first 50 bases



