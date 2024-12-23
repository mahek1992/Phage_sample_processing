import subprocess

# Define the input and output file paths
input_fasta = 'sheep_SEQ_COUNT_AS_HEADER.txt'
output_file = "sheep_igblast.tsv"
# Define the IgBLAST command
igblast_cmd = [
    'igblastn',
    '-query', input_fasta,
    '-out', output_file,
    '-germline_db_V', 'AlpacaV',
    '-germline_db_J', 'AlpacaJ',
    '-germline_db_D', 'AlpacaD',
    '-auxiliary_data','camelid_gl.aux',
    '-num_threads', '2',
    '-outfmt', '19',  
    # Add more parameters as needed, e.g., '-domain_system', 'imgt'
]

# Run the IgBLAST command
try:
    subprocess.run(igblast_cmd, check=True)
    print("IgBLAST analysis complete. Output saved to:", output_file)
except subprocess.CalledProcessError as e:
    print("Error running IgBLAST:", e)
