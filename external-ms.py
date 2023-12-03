import os
import heapq

def external_merge_sort(input_file, output_file, chunk_size):
    # Step 1: Divide the input into sorted chunks and write them to temporary files
    temp_files = []
    with open(input_file, 'r') as infile:
        chunk = []
        while True:
            line = infile.readline().strip()
            if not line:
                break
            chunk.append(line)
            if len(chunk) == chunk_size:
                chunk.sort()
                temp_file = f'temp/temp_{len(temp_files)}.txt'
                temp_files.append(temp_file)
                with open(temp_file, 'w') as temp:
                    temp.write('\n'.join(chunk))
                chunk = []
        # if the input file elements aren't divisible by the chunk size, there'll be remaining elments, sort them:
        if chunk:
            chunk.sort()
            temp_file = f'temp_{len(temp_files)}.txt'
            temp_files.append(temp_file)
            with open(temp_file, 'w') as temp:
                temp.write('\n'.join(chunk))

    # Step 2: Perform k-ways merge on the sorted chunks
    with open(output_file, 'w') as outfile:
        # Initialize a heap to perform the k-ways merge
        heap = []
        temp_file_handles = []

    # priority line?
        for temp_file in temp_files:
            temp_file_handle = open(temp_file, 'r')
            line = temp_file_handle.readline().strip()
            if line:
                heapq.heappush(heap, (line, temp_file_handle))
                temp_file_handles.append(temp_file_handle)

        # Perform the k-ways merge
        while heap:
            value, temp_file_handle = heapq.heappop(heap)
            outfile.write(value + '\n')
            next_line = temp_file_handle.readline().strip()
            if next_line:
                heapq.heappush(heap, (next_line, temp_file_handle))

        # Close all temporary file handles
        for temp_file_handle in temp_file_handles:
            temp_file_handle.close()

    # Step 3: Clean up temporary files
    for temp_file in temp_files:
        os.remove(temp_file)

# Example usage:
input_file = 'inputs/1m.txt/1m.txt'
output_file = 'outputs/1m-sorted.txt'

while True:
    escolha = input("\n1 - 5 Megabytes\n2 - 100 Megabytes\nEscolha o limite de memória que o programa utilizará: ")
    if (escolha == "1"):
        chunk_size = 150000
        break
    elif (escolha == "2"):
        chunk_size = 3000000
        break
    else:
        print("Insira uma opção válida!")

external_merge_sort(input_file, output_file, chunk_size)


# 150000 =~ 5mb
# 3000000 =~ 100mb
# 15000000 =~ 500mb
