# !pip install zipfile
# !sudo apt-get install unrar
# !pip uninstall pillow
# !pip install pillow --upgrade --force-reinstall
# # !pip install pillow
import zipfile
import io
import requests
from PIL import Image
import subprocess
# caso essa variavel nao seja definida como None as "tifs" ultrapassam o limite maximo de pixe default
Image.MAX_IMAGE_PIXELS = None
# funcao carrega as imagens contidas no disco
def carregarLocal():
  # arquivo usado para identificar o nome das imagens salvas
  # o mesmo e criado na primeira execuçao do codigo quando os tifs ainda nao foram descarregados
  with open("names.txt","r") as names:
    namelisted = names.readlines()
  # percorre o arquivo buscando a abertura de todos os nome nele contidos
  for imagen in namelisted:
      with open(imagen.replace("/","//").replace("\n",""),"rb") as image:
  # retorna o binario de cada um deles
        yield image.read()
# lista quee armazenara as imagens carregadas do disco
imagens = []
try:
  # tenta carregar localmente as imagens
  for imagenBTS in carregarLocal():
    imagens.append(io.BytesIO(imagenBTS))
# caso nao encontre localmente ele descarrega descompacta e salva a imagen em disco
except:
  print("arquivos nao encontrados no local, baixando do drive")
  link = "link do zip...nele contem uma pasta com imagens tif"
  response = requests.get(link)
  response.raise_for_status()
  print(len(response.content),"bytes baixados")
  bts = io.BytesIO(response.content)
  with zipfile.ZipFile(bts) as zf:
    zf.extractall()
    with open("names.txt","w") as names:
      names.write("\n".join(zf.namelist()[1:]))
    # apos gravar as imagens em disco as mesmas sao carregadas do local
    # sei que estou sendo redundante e ja que ja estao em memoria poderia simplesmente carrecarlas diretament edo buffer mas optei por fazer dessa forma para deixar mais legivel a intencao do codigo
  for imagenBTS in carregarLocal():
    imagens.append(io.BytesIO(imagenBTS))


def newArea(sections,size,dispercao = (10,10)):
    # sections == tamanho das imagens de saida
    # size == tamanho total do tif
    xdisp,ydisp = dispercao
    largura,altura = sections
    width,height  = size
    for x in range(width):
        for y in range(height):
            if x%xdisp == 0 and y%ydisp == 0:
                left = x
                upper = y
                right = x+largura
                lower = y+altura
                yield (left,upper,right,lower)
def aproved(image,usability):
    if image.mode != "RGBA":
        return True
    width,height  = image.size
    total = width*height
    transparentes = 0
    for x in range(width):
        for y in range(height):
            r,g,b,a = image.getpixel((x,y))
            if a < 10:
                transparentes += 1
                if transparentes > total*usability:
                    return False


def getSegmentos(img,sections,dispercao,USABLE):
  for area in newArea(sections,img.size):
    segmento = img.crop(area)
    if aproved(segmento,USABLE):
      yield segmento

for imagem in imagens:
  with Image.open(imagem,formats=["TIFF"]) as img:
    print(*getSegmentos(
        img=img,sections = (1000,1000),
        dispercao = (10,10),
        USABLE = 0.7),sep="\n")
    print("nSegments")
