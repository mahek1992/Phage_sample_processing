
from itertools import zip_longest
import os
import time
import tempfile
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import shutil
from multiprocessing import Pool, Manager
start_time = time.time()
def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

def process_file(folder_name, sequence_with_max_count, n):
    passed = []
    failed = []

    for filename in os.listdir(folder_name):
        #print(filename)
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_name, filename)
            with open(filepath, 'r') as file_2:
                sequence_file2 = [line.strip() for line in file_2]
                for line in sequence_file2:
                    seq, count = line.split(':')
                    mismatch_count = 0
                    if len(seq) == len(sequence_with_max_count):
                        mismatch_count = sum(1 for i in range(len(seq)) if seq[i] != sequence_with_max_count[i])
                        
                        if mismatch_count <= n:
                            passed.append(line)
                        else:
                            failed.append(line)
                    else:
                        failed.append(line)

    result_filename = f'{max_key}_{len(remain_strings)}.txt'
    result_filepath = os.path.join('/mnt/storage-HDD05a/1.scrach/immuno-mahek/WS1-scrach/crp/result/' + result_filename)
    with open(result_filepath, 'w') as file_2:
        for p in passed:
            file_2.write(f'{p}_maxkey{max_key}\n')

    final_passed = [p.split(':')[0] for p in passed]

    return final_passed, failed

    import concurrent.futures
    l = 32
    final_passed = []
    for p in passed:    
        seq_p = p.split(':')[0]
        final_passed.append(seq_p)

with open('sorted_sheep_light.txt', 'r') as file:
    strings = [line.strip() for line in file]

remain_strings = strings.copy()

total_files = 32
lines_per_file = len(remain_strings) // total_files + 1
file_counter = 1
with open('sheep_light_con.txt', 'a') as file:
    while remain_strings:
        count_passed = 0
        count_1 = 0
        failed = []
        sequence = [line.split(':')[0] for line in remain_strings]
        count = [int(line.split(':')[1].strip()) for line in remain_strings]

        max_key = max(count)
        if max_key < 20:
            print('max_key is less than 20')
            break

        n = 3 if max_key in range(2, 400) else 4 if max_key in range(410, 1000) else 5 if max_key > 1000 else 10
        sequence_with_max_count = sequence[count.index(max(count))]

        lines_per_file = len(remain_strings) // total_files + 1
        folder_name = f"{max_key}_{len(remain_strings)}_files"
        os.makedirs(folder_name, exist_ok=True)
        for file_counter, lines_chunk in enumerate(grouper(lines_per_file, remain_strings), start=1):
            lines_chunk = [line for line in lines_chunk if line is not None]
            lines_to_write = len(lines_chunk)
            temp_file_name = f"temp_{file_counter}_{len(remain_strings)}.txt"
            with open(os.path.join(folder_name, temp_file_name), 'w') as fout:
                for s in lines_chunk:
                    fout.write(f'{s}\n')
                    
            new_filename = os.path.join(folder_name, f'small_file_{len(lines_chunk)}_{file_counter}.txt')
            shutil.move(fout.name, new_filename)
        with ThreadPoolExecutor(max_workers=32) as executor:
            
            results = list(executor.map(
                process_file,
                [folder_name],
                [sequence_with_max_count],
                [n]
            ))

        for result, remaining_strings in results:   
            failed.extend(remaining_strings)
        remain_strings = failed.copy()     
        shutil.rmtree(folder_name)
end_time = time.time() 
print(f"Script started at: {time.ctime(start_time)}")
print(f"Script ended at: {time.ctime(end_time)}")
