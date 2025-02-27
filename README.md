
# TODO

Em ordem de prioridade:


1) Inserção de mais classes (binária: milho e daninha)

- Os dados precisam ser rotulados usando anotações da imagem, use ferramentas (e.g. VGG VIA) para facilidade na construção dos polígonos e exportação de um JSON

```
{
  "shape_attributes": { ... },
  "region_attributes": {
    "classe": "milho"
  }
}
{
  "shape_attributes": { ... },
  "region_attributes": {
    "classe": "daninha"
  }
}
```

- Rotule POUCAS IMAGENS com dataset e faça o teste de captura pelo modelo das duas classes! Você precisará modificar o código para isso, alterar thing_classes, treinar o modelo com as duas classes, em diante. Uma vez validado o JSON, siga adiante! 


2) Contagem das classes preditas
 
```
pred_classes = outputs["instances"].pred_classes.cpu().numpy()
num_milho = np.sum(pred_classes == 0)
num_daninha = np.sum(pred_classes == 1)

print("Milho detectado:", num_milho)
print("Daninha detectada:", num_daninha)
```

3) Identificar espaçamento entre plantas (densidade)

```
# Uma sugestão é calcular a distância em pixels entre um objeto (centro) e outro

boxes = outputs["instances"].pred_boxes.tensor.cpu().numpy()
# boxes[i] = [x1, y1, x2, y2]
# Centro:
centers = []
for box in boxes:
    x1, y1, x2, y2 = box
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    centers.append((cx, cy))  
# Filtre só as detecções de milho ou daninha usando pred_classes
```

# Otimização

* Data Augmentation
* PointRend



