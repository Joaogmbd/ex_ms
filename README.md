# Documentação do Código

## Ordenação utilizando chunks

```py
def external_merge_sort(input_file, output_file, chunk_size):
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
    if chunk:
        chunk.sort()
        temp_file = f'temp_{len(temp_files)}.txt'
        temp_files.append(temp_file)
        with open(temp_file, 'w') as temp:
            temp.write('\n'.join(chunk))
```

A primeira parte do código contempla a organização dos elementos do arquivo de entrada, utilizando chunks para o controle do uso de memória. (Os tamanhos dos chunks podem ser entendidos como número de linhas por arquivo temporário).

**A primeira** condição é uma verificação de linha vazia, o que determinaria o fim do arquivo de input. Ao ler uma linha "vazia", esse looping é finalizado.

**A segunda** condição imposta é quando a quantidade de linhas chega ao numero de chunks definido. Nesse ponto, o programa realiza a ordenação nas linhas já lidas, utilizando o arquivo temporário de caminho pré-definido no código(diretorio temp). A nomeação de cada arquivo é baseada em seu indice no array "temp_files". No final da inserção de todas as linhas em cada arquivo temporário, a varivel chunk é resetada, e o looping While faz com que o programa continue a partir da linha seguinte.

**A terceira** condição do código é um tratamento, para caso o numero de elementos do arquivo não seja divisivel pelo tamanho do chunk definido, as linhas remanescentes sejam organizadas.


## Junção dos Arquivos temporários
```py
with open(output_file, 'w') as outfile:
    # Initialize a heap to perform the k-ways merge
    heap = []
    temp_file_handles = []

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

```

Na segunda parte do código, temos a implementação do k-ways merge e a construção do arquivo de saída final. Essa implementação garante que ao juntar os arquivos temporários em um único arquivo, este estará ordenado devidamente.

**O primeiro** looping percorre cada arquivo temporário, coletando o primeiro elemento (que será sempre o menor de cada arquivo) e populando o nó do heap com esse elemento e o seu respectivo arquivo.

**O segundo** looping é a inserção do menor elemento do heap ao arquivo final. A cada inserção, o elemento é removido do heap, e a próxima linha do mesmo arquivo temporário deste elemento é inserida no heap, e assim é feito até acabarem as linhas de todos os arquivos temporários.

**O terceiro** looping é o fechamento de cada arquivo temporário que foi utilizado no heap.

```py
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
```

Essa é a parte final do código, onde é definido o caminho para o arquivo de input e o arquivo onde ficará a saída final do programa, com todos os elementos organizados.

A condição foi definida com base na solicitação da atividade feita pelo professor, onde devemos selecionar se queremos organizar o arquivo menor (com 1 milhão de entradas) ou o arquivo maior (com 500 milhões de entradas). Essa escolha define o tamanho do chunk utilizado na primeira parte do código.

## Chunk size para MB

### 150000 =~ 5mb
### 3000000 =~ 100mb
### 15000000 =~ 500mb
