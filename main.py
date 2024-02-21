# Instrucoes
# 1. Definir caminho da fonte
# 2. Definir tamanho da fonte
# 3. Definir caminho da imagem
# 4. Definir coordenada y do texto (x é alterada calculando para centralizar)
# 5. Definir cor do texto
# 6. Executar o script -> "python3 nome_deste_arquivo.py < arquivo_com_nomes.txt"
#
# O arquivo de texto com nomes deve ser na forma:
# Inteiro indicando quantidade de nomes que devem ser lidos pelo script
# Lista com os nomes, um por linha
#
# Pode ser necessário executar algumas vezes o script para encontrar a posição desejada para a coordenada y



from PIL import Image, ImageDraw, ImageFont

# Define caminho e tamanho da fonte
caminho_fonte = 'caminho/para/fonte/fonte.ttf'
tam_fonte = 12
font = ImageFont.truetype(caminho_fonte, size=tam_fonte)

# Imagem a ser modificada
caminho_imagem = 'caminho/para/imagem/imagem.png'

# Define posicao inicial do texto
x = 0  # coordenada x na imagem (é definida baseada no tamanho da imagem e do nome, valor 0 apenas para inicializacao)
y = 86 # coordenada y na imagem
cor = '#7d19b8' # cor do texto

idx = 1 # variavel auxiliar para loop
q = int(input()) # quantidade de nomes a serem lidos (primeira linha do arquivo)
print(f"Executando o script para {q} nomes:\n")
for _ in range(q):
    name = input().strip().upper()
    print(f"{idx}. {name}")

    # Open the PNG image
    image = Image.open(caminho_imagem)
    
    # Ajusta coordenada x considerando tamanho do nome
    comprimento, altura = image.size # caracteristicas da imagem
    comp_nome_pixels = font.getlength(name) # calcula comprimento do nome em pixels
    x = int((comprimento - comp_nome_pixels) // 2) # ajusta coordenada x

    # Create a drawing context
    draw = ImageDraw.Draw(image)
    
    # Write name in image
    draw.text((x, y), name, fill=cor, font=font)

    # Save the modified image
    nome_arquivo = name.replace(" ", "_")
    image.save(f"{nome_arquivo}.png")

    # Close the image
    image.close()

    idx += 1
