import heapq
import sys

# essa função eh a primeira parte do external merge sort, onde os dados sao separados em fragmentos 
# e organizados separadamente.
def cria_fragmento_organizado(caminho_do_arquivo, tam_frag):
    fragmentos = []
    with open(caminho_do_arquivo, 'r') as file:
        frag = []
        for linha in file:
            frag.append(str(linha.strip()))
            # preenche o fragmento com as linhas lidas do arquivo, até chegar no tamanho declarado "tam_frag"
            if len(frag) == tam_frag:
                frag.sort()
                fragmentos.append(frag)
                frag = []

        # se ainda sobram dados que nao se encaixam na quantidade declarada para o tamanho do fragmento, organize-os
        if frag:
            frag.sort()
            fragmentos.append(frag)

    return fragmentos

# agora no segundo passo, juntamos os fragmentos em um arquivo unico de output,
# onde todos os dados estão organizados

# A estrutura de dados escolhida para fazer o merge dos fragmentos é a heap (exige pouco recurso para acessar grandes conjuntos de dados).
# Por isso o import na biblioteca "heapq"

def juntar_frag_organizados(fragmentos, caminho_saida):
    # declaracao de min_heap (arv. binaria completa, onde o valor de um nó é sempre menor que o valor de seus filhos)
    heap = [(frag[0], i, 0) for i, frag in enumerate(fragmentos) if frag]
    heapq.heapify(heap)

    # pega o minimo valor do heap, e escreve no arquivo de saída
    with open(caminho_saida, 'w') as arquivo:
        while heap:
            valor, frag_indice, elemento_indice = heapq.heappop(heap)
            arquivo.write(str(valor) + '\n')

            # coloca os proximos elementos do fragmento no heap.
            if elemento_indice + 1 < len(fragmentos[frag_indice]):
                prox_elemento = fragmentos[frag_indice][elemento_indice + 1]
                heapq.heappush(heap, (prox_elemento, frag_indice, elemento_indice + 1))

# chama as duas funções criadas
def merge_sort_externo(caminho_do_arquivo, caminho_saida, tam_frag):
    fragmentos = cria_fragmento_organizado(caminho_do_arquivo, tam_frag)
    juntar_frag_organizados(fragmentos, caminho_saida)

# use os argumentos da linha de comando para passar os valores da variaveis abaixo 

caminho_do_arquivo = sys.argv[1]
caminho_saida = sys.argv[2]
tam_frag = sys.argv[3]

merge_sort_externo (caminho_do_arquivo, caminho_saida, tam_frag)