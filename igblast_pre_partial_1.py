from Bio import SeqIO

def is_match_with_one_mismatch(seq, target):
    # Compare the target with the sequence allowing at most 1 mismatch
    differences = sum(1 for a, b in zip(seq, target) if a != b)
    return differences <= 1

def split_sequence(sequence, target="GAAGGTAAATCTTCTGGCTCTGGCTCTGAG"):
    part1 = None
    part2 = None

    truncated_sequence = sequence[:200]
    

    for i in range(len(truncated_sequence) - len(target) + 1):
        subseq = truncated_sequence[i:i + len(target)]
        if is_match_with_one_mismatch(subseq, target):

            part1 = sequence[:i + len(target)]
            part2 = sequence[i:]
            break
            
    return part1, part2


def process_fasta(input_fasta, part1_output, part2_output, target="GAAGGTAAATCTTCTGGCTCTGGCTCTGAG"):
    part1_seqs = []
    part2_seqs = []
    
    
    for record in SeqIO.parse(input_fasta, "fasta"):
        sequence = str(record.seq)
        
        part1, part2 = split_sequence(sequence, target)
        
        if part1 and part2:  # If a match was found
            
            part1_seqs.append(f">{record.id}\n{part1}")
            part2_seqs.append(f">{record.id}\n{part2}")
    
    
    with open(part1_output, "w") as part1_file:
        part1_file.write("\n".join(part1_seqs))
    
    with open(part2_output, "w") as part2_file:
        part2_file.write("\n".join(part2_seqs))


input_fasta = "/home/mahek0423/sheep/sheep_heavy_light_con_file.txt"  # Input FASTA file
part1_output = "/home/mahek0423/sheep/part1.fasta"  # Output file for part 1
part2_output = "/home/mahek0423/sheep/part2.fasta"  # Output file for part 2

process_fasta(input_fasta, part1_output, part2_output)
