import json
import os
import cv2
import numpy as np

class createMascsFrom:
    def __init__(self, path, imgExt):
        self.path = path
        self.imgExt = imgExt
        self.imgs = [img for img in os.listdir(path) if self.extentions(img)]
        self.json = [
            os.path.join(path, _json) 
            for _json in os.listdir(path) 
            if _json.endswith('json')
        ]
        if len(self.json) > 1:
            jsons = ''.join([f'{i}{option}\n' for i, option in enumerate(self.json)])
            self.arqMap = self.json[
                int(input(f'''Qual o arquivo de mapeamento?\n{jsons}'''))
            ]
        else:
            self.arqMap = self.json[0]
        self.getImageJsons()

    def getImageJsons(self):
        with open(self.arqMap, 'r') as armap:
            self.ImageObjects = json.load(armap)
            if len(self.ImageObjects) > len(self.imgs):
                print('>>>>>>>>>>>>>>>>>>>>>>', self.ImageObjects)
                print('>>>>>>>>>>>>>>>>>>>>>>', self.imgs)
                raise ValueError("Há mais anotações do que imagens")

    def getImages(self):
        return self.imgs
    
    def getImagesPaths(self):
        return [os.path.join(self.path, img) for img in self.imgs]

    def extentions(self, img):
        for ext in self.imgExt:
            if img.endswith(ext):
                return True
        return False

    def getRegions(self):
        for image_name, ImageObject in self.ImageObjects.items():
            path_image = os.path.join(self.path, image_name)
            yield image_name,path_image, self.getSize(path_image), ImageObject['regions']

    @staticmethod
    def getSize(path_image):
        image = cv2.imread(path_image)
        if image is None:
            raise FileNotFoundError(f"A imagem no caminho '{path_image}' não pôde ser carregada.")
        altura, largura, _ = image.shape
        return (largura, altura)


def generate_masks(image_name,out_path, image_size, regions):
    width, height = image_size
    
    # Identificar os tipos únicos e mapear para cores distintas
    unique_types = list(set(region["region_attributes"]["type"] for region in regions))
    type_to_color = {t: int(255 * (i + 1) / len(unique_types)) for i, t in enumerate(unique_types)}
    
    # Criar uma única máscara para todos os tipos
    mask = np.zeros((height, width), dtype=np.uint8)
    
    for region in regions:
        shape = region["shape_attributes"]
        all_points_x = shape["all_points_x"]
        all_points_y = shape["all_points_y"]
        pts = np.array([list(zip(all_points_x, all_points_y))], dtype=np.int32)
        
        region_type = region["region_attributes"]["type"]
        color = type_to_color[region_type]
        
        # Preencher o polígono na máscara com a cor correspondente ao tipo
        cv2.fillPoly(mask, pts, color)
    
    # Salvar a máscara
    out_image_path = os.path.join(out_path, f"mask_{os.path.basename(image_name)}")
    cv2.imwrite(out_image_path, cv2.resize(mask, (width*2, height*2)))


if __name__ == '__main__':
    path = r'.\testeImageAnnotator'
    out_path = r'.\testeImageAnnotator\out'
    imgExt = ['jpg']
    mascs = createMascsFrom(path, imgExt)

    for image_name,path_image, image_size, regions in mascs.getRegions():
        generate_masks(image_name,out_path, [int(tam / 2) for tam in image_size], regions)
