import os
import cv2
import numpy as np
from mtcnn import MTCNN
from deepface import DeepFace
import faiss
import matplotlib.pyplot as plt  

# Inicializando o detector de rostos MTCNN
detector = MTCNN()

def detectar_rosto(caminho_img):
    """Detecta o rosto na imagem e retorna apenas a área do rosto."""
    img = cv2.imread(caminho_img)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

   
    deteccoes = detector.detect_faces(rgb_img)

    if len(deteccoes) == 0:
        print(f"Nenhum rosto encontrado em {caminho_img}.")
        return None

    
    x, y, largura, altura = deteccoes[0]['box']
    rosto = rgb_img[y:y + altura, x:x + largura]

    return rosto

def calcular_embedding(imagem):
    """Calcula o embedding de uma imagem usando DeepFace."""
    embedding = DeepFace.represent(imagem, model_name="Facenet", enforce_detection=False)
    return embedding[0]['embedding']

def salvar_embeddings(pasta_imagens, arquivo_embeddings="embeddings.npy"):
    """Salva os embeddings das imagens de uma pasta."""
    embeddings = []
    imagens = []

    for arquivo in os.listdir(pasta_imagens):
        if not arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        caminho_img = os.path.join(pasta_imagens, arquivo)
        rosto = detectar_rosto(caminho_img)

        if rosto is None:
            continue

        embedding = calcular_embedding(rosto)
        embeddings.append(embedding)
        imagens.append(caminho_img)

    embeddings = np.array(embeddings)
    np.save(arquivo_embeddings, embeddings)
    return imagens, embeddings

def carregar_embeddings(arquivo_embeddings="embeddings.npy"):
    """Carrega os embeddings de um arquivo."""
    embeddings = np.load(arquivo_embeddings)
    return embeddings

def comparar_com_pasta(img_referencia_path, pasta_imagens, model_name="Facenet"):
    

    rosto_referencia = detectar_rosto(img_referencia_path)
    if rosto_referencia is None:
        print("Não foi possível encontrar um rosto na imagem de referência.")
        return

    embedding_referencia = calcular_embedding(rosto_referencia)

    # Salvar embeddings se não existirem
    arquivo_embeddings = "embeddings.npy"
    if not os.path.exists(arquivo_embeddings):
        imagens, embeddings = salvar_embeddings(pasta_imagens, arquivo_embeddings)
    else:
        imagens = os.listdir(pasta_imagens)
        embeddings = carregar_embeddings(arquivo_embeddings)

    
    dimension = embeddings.shape[1]  
    quantizer = faiss.IndexFlatL2(dimension)  
    index = faiss.IndexIVFFlat(quantizer, dimension, 2, faiss.METRIC_L2)  
    if not index.is_trained:
        index.train(embeddings)  
    index.add(embeddings)  

    
    k = 5  
    D, I = index.search(np.array([embedding_referencia]), k)  

    print("\nAs 5 imagens mais próximas são:")
    for i, idx in enumerate(I[0]):
        if idx == -1: 
            continue
        caminho_img = os.path.join(pasta_imagens, imagens[idx])  
        
        
        similaridade = 1 / (1 + D[0][i])  
        similaridade = similaridade * 100  

        if similaridade < 0:  
            similaridade = 0
        elif similaridade > 100:  
            similaridade = 100
        
        print(f"{i + 1}. {caminho_img} - Similaridade: {similaridade:.2f}%")
        
        # Exibição da imagem
        img = cv2.imread(caminho_img)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img_rgb)
        plt.title(f"Imagem {i + 1} - Similaridade: {similaridade:.2f}%")
        plt.axis('off')
        plt.show()


# Exemplo de uso
img_referencia = os.path.join(os.path.dirname(__file__), "dele.jpeg")
pasta = os.path.join(os.path.dirname(__file__), "fotosT")


comparar_com_pasta(img_referencia, pasta)
