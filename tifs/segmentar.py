from PIL import Image
import os
import sys

Image.MAX_IMAGE_PIXELS = None  # Remove o limite de pixels

# Verifica se um argumento foi passado
if len(sys.argv) < 2:
    print("Uso: python segmentador.py <nome_da_imagem>")
    sys.exit(1)

# Obtém o nome da imagem a partir dos argumentos
path = sys.argv[1]

# Verifica se o arquivo existe
if not os.path.isfile(path):
    print(f"Erro: O arquivo '{path}' não foi encontrado.")
    sys.exit(1)

# Obtém o nome base da imagem sem extensão
nome_base = os.path.splitext(os.path.basename(path))[0]

# Cria um diretório com o nome da imagem
output_dir = os.path.join(os.path.dirname(path), nome_base)
os.makedirs(output_dir, exist_ok=True)

# Função para verificar transparência
def calcular_transparencia(img):
    if img.mode != "RGBA":
        return 0  # Se não for RGBA, não há transparência
    
    pixels = img.getdata()
    total_pixels = len(pixels)
    pixels_transparentes = sum(1 for p in pixels if p[3] < 128)

    return (pixels_transparentes / total_pixels) * 100  # Retorna a porcentagem de transparência

# Função para verificar pixels pretos
def calcular_pixels_pretos(img):
    if img.mode == "RGBA":
        img = img.convert("RGB")  # Converte para RGB se necessário
    
    pixels = img.getdata()
    total_pixels = len(pixels)
    pixels_pretos = sum(1 for p in pixels if p == (0, 0, 0))

    return (pixels_pretos / total_pixels) * 100  # Retorna a porcentagem de preto

# Função para dividir a imagem em blocos menores
def subdividir_e_exportar(imagem, tamanho_bloco=512):
    largura, altura = imagem.size
    contador = 1  # Contador para nomear os arquivos sequencialmente
    total_blocos = (largura // tamanho_bloco + 1) * (altura // tamanho_bloco + 1)  # Total de blocos previstos

    for y in range(0, altura, tamanho_bloco):
        for x in range(0, largura, tamanho_bloco):
            # Recorta um bloco da imagem
            caixa = (x, y, min(x + tamanho_bloco, largura), min(y + tamanho_bloco, altura))
            subimagem = imagem.crop(caixa)

            # Verifica transparência e pixels pretos
            transparencia = calcular_transparencia(subimagem)
            pretos = calcular_pixels_pretos(subimagem)

            if transparencia > 70 or pretos > 30:
                continue  # Pula imagens com muita transparência ou preto

            # Define nome do arquivo
            nome_arquivo = os.path.join(output_dir, f"{contador}.jpg")

            # Ajusta qualidade para manter abaixo de 1MB
            qualidade = 95
            while True:
                subimagem.convert("RGB").save(nome_arquivo, "JPEG", quality=qualidade)
                if os.path.getsize(nome_arquivo) < 1_000_000 or qualidade <= 10:
                    break
                qualidade -= 5  # Reduz a qualidade até ficar abaixo de 1MB

            print(f"Imagem {contador} de {total_blocos} processada...")  # Atualiza o progresso
            
            contador += 1  # Incrementa o contador para o próximo nome de arquivo

# Carrega a imagem e inicia o processo
try:
    with Image.open(path) as img:
        subdividir_e_exportar(img)
    print(f"Processo concluído! As imagens foram salvas em: {output_dir}")
except Exception as e:
    print(f"Erro ao processar a imagem: {e}")
