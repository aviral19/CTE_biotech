from Bio import SeqIO

for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    #prints the records id
    print(seq_record.id)
    #Returns the sequence
    print(repr(seq_record.seq))
    #Returns the length of the sequence
    print(len(seq_record))
