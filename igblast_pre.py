from Bio import SeqIO

input_fastq_file_5g = "sheep_con_file.txt"

output_file_full = "sheep_SEQ_COUNT_AS_HEADER.txt"


sequence_full_list = []
sequence_list_only = []

with open(output_file_full, 'w') as file:
    for i, record in enumerate(SeqIO.parse(input_fastq_file_5g, "fasta")):
        header_parts = record.description.split("_")
        header = f"> {header_parts[0]}"
        print(header)
        sequence_data_5g = str(record.seq)
        print(sequence_data_5g)
        sequence_full_list.append(f"{header}\n{sequence_data_5g}")
        sequence_list_only.append(header_parts[2].strip())

    

    for seq_full in sequence_full_list:
        file.write(seq_full + '\n')

# Save the sequence_list_only to a file
print("List of sequence headers only:", sequence_list_only)
