# Abelardo_luz
import os

# Caminho da pasta com as imagens
pasta_imagens = r"C:\Users\Angelo\Documents\IC_Milho_Acompanhamento\tifs\Ponta_Grossa"  # Substitua pelo caminho correto

# Obtém todos os arquivos na pasta
arquivos = os.listdir(pasta_imagens)

# Filtra apenas os arquivos .jpg com nomes numéricos
imagens = [arquivo for arquivo in arquivos if arquivo.endswith(".jpg") and arquivo.split('.')[0].isdigit()]

# Solicita o nome do usuário
nome_input = input("Digite o nome para renomear as imagens: ")

# Renomeia as imagens
for i, imagem in enumerate(imagens, start=1):
    # Novo nome para a imagem
    novo_nome = f"{nome_input}{i}.jpg"
    
    # Caminho completo da imagem antiga e nova
    caminho_antigo = os.path.join(pasta_imagens, imagem)
    caminho_novo = os.path.join(pasta_imagens, novo_nome)
    
    # Renomeia o arquivo
    os.rename(caminho_antigo, caminho_novo)
    
    print(f"Renomeado {imagem} para {novo_nome}")

print("Renomeação concluída!")
