# IC_Milho_Acompanhamento
Repositrio destinado ao desenvolvimento da Iniciação Científica (IC) de fenotipagem do milho. Segue o link para acesso ao projeto no Colab:  [Colab IC_Milho_Acompanhamento.ipynb](https://colab.research.google.com/drive/1VyvdgFo0VYL7NHEjM6M1uZzDO8zSyl_9?usp=sharing) Comentários, dicas e críticas construtivas são sempre bem-vindos!

**11/12** **Descrição do Software**
O software foi desenvolvido para processar imagens compactadas em um arquivo ZIP armazenado no Google Drive e gerar um mapa vetorial indicando os segmentos de interesse com base na transparência dos pixels.

Funcionalidades Principais
Download e Descompactação:

A biblioteca requests é utilizada para baixar o arquivo compactado diretamente do Google Drive.
O conteúdo do arquivo ZIP é extraído usando zipfile, com io manipulando os dados em buffer para evitar acessos desnecessários ao disco.
Processamento de Imagens:

As imagens TIFF descompactadas são analisadas pela biblioteca Pillow (PIL).
O software percorre cada imagem como um mapa, identificando áreas onde a transparência é inferior a 30% dos pixels.
Geração do Mapa Vetorial:

A partir da análise, é gerado um mapa vetorial que indica as regiões segmentadas de interesse.
Este mapa vetorial serve como uma representação compacta e eficiente das áreas a serem capturadas, reduzindo o uso de armazenamento e facilitando o processamento posterior.
Automação com Comandos Externos:

A biblioteca subprocess é utilizada para executar comandos automatizados que complementam o fluxo de trabalho, quando necessário.
Fluxo de Operação
O software faz o download do arquivo ZIP armazenado no Google Drive.
Os arquivos TIFF são descompactados em buffer, evitando gravações intermediárias no disco.
Cada imagem é processada, identificando segmentos com transparência inferior a 30%.
Um mapa vetorial é gerado, representando as áreas relevantes para captura.
Resultado
O resultado final é um mapa vetorial que destaca as regiões segmentadas nas imagens. Este mapa pode ser utilizado para análises posteriores ou integrado a outros sistemas que demandem uma representação precisa e eficiente dos dados processados.
[001.py](https://github.com/AngeloDev-New/IC_Milho_Acompanhamento/blob/main/Scripts/001.py)

**12/12**
Conforme comentado no grupo de controle do WhatsApp, o protótipo inicial de segmentação não funcionou como o esperado. Contudo, foi uma rica fonte de aprendizado para mim. Pretendo continuar utilizando a base de carregamento como está, mas, com base no livro [Python para Análise de Dados](https://www.amazon.com.br/Python-Para-An%C3%A1lise-Dados-Tratamento/dp/8575226479/ref=sr_1_2?adgrpid=1141293730226964&dib=eyJ2IjoiMSJ9.UYPX3cU1vlR1g5ka256QBQFSnrYDxyHANJrJMX9Syr8pwzZOp0B8yEITq9VdYiiFJPoSckle3TnBiUbvNmT97BnvEmej5nt-4ZlmR5m-iGLmxmpH5kVKWaECiT93S7_6fws2uCMqGm6Zsd36qxiQ3JIJVlpsBs-WPU5rJ7zliOtnvn5iAKUZmZxG-VPf-mnC0n-XA6CG842poP7R5n0q6qgwfNRrEu8w1oFPMxvj1J1GoAgLI-3H8M6eeUP-RN443_Mlkb0Y6S00ldXXocMDqL61A2Cu8wudO_oBvJF_8GaWWp8LOEdc6ZC1I_fNBFsGem5vsF_IyZdZf_vwEPfK67HkMGS9f3LhuKKpurFe_PgUXd9H6dstCGTNXkIZy4BFnNBPDEE1IoqUiDxlooM4y-OjK445utdsb9AHwQupI377dIFanLdFb_QnbzOiOG-e.UXyuego9Sj3dOlkieXC62FCJj61sJtr77BD7x_qJ4sg&dib_tag=se&hvadid=71330944898389&hvbmt=be&hvdev=c&hvlocphy=184997&hvnetw=o&hvqmt=e&hvtargid=kwd-71331374786960%3Aloc-20&hydadcr=5714_11235317&keywords=python+para+an%C3%A1lise+de+dados+wes+mckinney&qid=1734019643&sr=8-2), que estou usando como referência de estudo, transformarei as imagens em arrays do NumPy. Essa abordagem permitirá melhorar significativamente a performance em futuras transformações, geração de máscaras e outras operações.
[002.py](https://github.com/AngeloDev-New/IC_Milho_Acompanhamento/blob/main/Scripts/002.py)

**12/12** Estamos enfrentando problemas de falta de memória, mas sem preocupação. A partir de agora, aplicarei técnicas aprendidas no curso [Segmentacao Imagens Python a-z](https://www.udemy.com/course/segmentacao-imagens-python-a-z/) fornecido pelo leo (meu orientador principal).

**13/12** ** * Limiarização ou binarização** é um método aplicado em imagens monocromáticas, ou seja, em escala de cinza. Nesse processo, define-se um valor de limiar entre 0 e 255, onde todos os pixels com valores acima desse limiar são convertidos para 255 (branco), enquanto os valores abaixo são convertidos para 0 (preto).

**13/12** Analisando a estrutura da nossa documentação, percebi que, ao inverter a ordem de apresentação e deixar as novidades no topo, o conteúdo se tornaria mais visível para mim e mais legível para os interessados. Além disso, foi criado o arquivo [Readme.md](https://github.com/AngeloDev-New/IC_Milho_Acompanhamento/tree/main#readme) do projeto no Git.
**16/12** aplicando binarizacao basica na imagem (a nivel de aprendizados estes processos iniciais serao aplicados na imagem ![img.png](https://raw.githubusercontent.com/AngeloDev-New/IC_Milho_Acompanhamento/refs/heads/main/img.png)) optei fazer tanto na mao pra entender a logica por traz quanto usando as facilidades do cv2 
![003.py](https://github.com/AngeloDev-New/IC_Milho_Acompanhamento/blob/main/Scripts/003.py)
Script esta setado com limiar 170 é gerou:

![THRESH_BINARY.png](https://raw.githubusercontent.com/AngeloDev-New/IC_Milho_Acompanhamento/refs/heads/main/imgs/THRESH_BINARY.png)

![THRESH_BINARY_INV.png](https://raw.githubusercontent.com/AngeloDev-New/IC_Milho_Acompanhamento/refs/heads/main/imgs/THRESH_BINARY_INV.png)

![THRESH_THRUNK.png](https://raw.githubusercontent.com/AngeloDev-New/IC_Milho_Acompanhamento/refs/heads/main/imgs/THRESH_TRUNC.png)

![THRESH_TOZERO.png](https://raw.githubusercontent.com/AngeloDev-New/IC_Milho_Acompanhamento/refs/heads/main/imgs/THRESH_TOZERO.png)
![THRESH_TOZERO_INV.png](https://raw.githubusercontent.com/AngeloDev-New/IC_Milho_Acompanhamento/refs/heads/main/imgs/THRESH_TOZERO_INV.png)
