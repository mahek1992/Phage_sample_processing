import csv

input_file = '/home/mahek0423/sheep/sheep_LK_igblast.csv'
output_file = '/home/mahek0423/sheep/sheepLK_file.csv'

with open(input_file, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    rows = list(reader)

if rows:
    headers = rows[0]
    # Only append '_heavy' if the header is not blank
    headers = [header + '_heavy' if header.strip() else header for header in headers]
    rows[0] = headers

with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print("Headers updated and saved to", output_file)
