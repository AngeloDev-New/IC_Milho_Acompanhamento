# !pip install zipfile
# !sudo apt-get install unrar
# !pip uninstall pillow
# !pip install pillow --upgrade --force-reinstall
# # !pip install pillow
import gc
import zipfile
import io
import requests
from PIL import Image
import subprocess
import numpy as np
Image.MAX_IMAGE_PIXELS = None
def base_de_carregamento(nImagensAResgatar = None):


  def carregarLocal():
    with open("names.txt","r") as names:
      namelisted = names.readlines()
      if nImagensAResgatar != None:
        namelisted = namelisted[:nImagensAResgatar]
    for imagen in namelisted:
        with open(imagen.replace("/","//").replace("\n",""),"rb") as image:
          yield image.read()
  imagens = []
  try:
    for imagenBTS in carregarLocal():
      imagens.append(io.BytesIO(imagenBTS))
  except:
    print("arquivos nao encontrados no local, baixando do drive")
    link = "...zip"
    response = requests.get(link)
    response.raise_for_status()
    print(len(response.content),"bytes baixados")
    bts = io.BytesIO(response.content)
    with zipfile.ZipFile(bts) as zf:
      zf.extractall()
      with open("names.txt","w") as names:
        names.write("\n".join(zf.namelist()[1:]))
    for imagenBTS in carregarLocal():
      imagens.append(io.BytesIO(imagenBTS))
  if len(imagens) == 1:
    return imagens[0]
  return imagens
  # o codigo acima nao esta comentado pois ja foi comentado no exemplo acima
################################
# apartir de aqui e codigo novo#
################################

imagem = Image.open(base_de_carregamento(1))

largura,altura = imagem.size
largura/=9
altura/=9
imagemar = np.array(imagem)[1]
del imagem
gc.collect()
Image.fromarray(imagemar).resize((int(largura),int(altura))).save("imagem_redimensionada.png")
# array_imagens = [np.array(imagen) for imagen in imagens]
