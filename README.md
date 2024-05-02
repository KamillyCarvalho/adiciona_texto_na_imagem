# colocaTextoNaImagem
Script que lê uma imagem e adiciona texto fornecido.

# Instruções
    1. Definir caminho da fonte
    2. Definir tamanho da fonte
    3. Definir coordenada y do texto (x é alterada calculando para centralizar)
    4. Executar o script -> "python3 nome_deste_arquivo.py < arquivo_com_nomes.txt"

O arquivo de texto com nomes deve ser na forma:
- Caminho da imagem que deve ser adicionado o texto
- Hex da cor do texto que será adicionado
- Inteiro indicando quantidade de nomes que devem ser lidos pelo script
- Lista com os nomes, um por linha

Pode ser necessário executar algumas vezes o script para encontrar a posição desejada para a coordenada **y**.
