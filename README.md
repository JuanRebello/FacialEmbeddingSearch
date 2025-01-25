# Facial Embedding Search
## Descrição

Este projeto é um sistema de comparação de rostos desenvolvido para realizar buscas em uma pasta contendo milhares de imagens. Ele utiliza detecção facial (MTCNN), embeddings gerados pelo DeepFace e a biblioteca FAISS para identificar e exibir as imagens mais similares ao rosto de referência.
As imagens mais similares são exibidas em ordem decrescente de similaridade (do maior para o menor percentual), onde a menor distância corresponde à maior similaridade.
Este sistema é ideal para aplicações de segurança e defesa que necessitam de comparação facial rápida e precisa.

## Funcionalidades

- Detecção de rostos em imagens utilizando MTCNN.
- Geração de embeddings faciais com DeepFace.
- Indexação eficiente com FAISS para buscas rápidas.
- Exibição das imagens mais similares com percentuais de similaridade.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados:

- Python 3.8 ou superior
- Virtualenv (opcional, mas recomendado)
- Dependências listadas no arquivo requirements.txt

## Instalação

 1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/FacialEmbeddingSearch.git

2. Acesse o diretório do projeto:
    ```bash
    cd FacialEmbeddingSearch

 3. Crie e ative um ambiente virtual (opcional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt

## Uso

1. Certifique-se de que você tem uma pasta contendo as imagens que deseja comparar e uma imagem de referência.
2. Atualize os caminhos da imagem de referência e da pasta no script principal.
3. Execute o script:
    ```bash
    python app.py
5. O programa exibirá as 5 imagens mais similares na pasta, junto com seus percentuais de similaridade, em ordem decrescente. A similaridade é calculada com base na distância euclidiana invertida.

## Estrutura do Projeto

- **app.py:** Script principal contendo toda a lógica do sistema.
- **requirements.txt:** Lista de dependências necessárias para executar o projeto.

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do repositório.

2. Crie um branch para suas alterações:
    ```bash
    git checkout -b minha-nova-feature

3. Envie suas alterações:
    ```bash
    git commit -m "Adicionei uma nova funcionalidade"

4. Faça um push para o branch:
    ```bash
    git push origin minha-nova-feature

5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.
