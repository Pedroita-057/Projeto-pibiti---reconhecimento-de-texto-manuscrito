
# Reconhecimento de Texto Manuscrito (PIBITI)

Sistema de reconhecimento de texto manuscrito (HTR) em português brasileiro, desenvolvido como parte do plano de trabalho de Iniciação em Desenvolvimento Tecnológico e Inovação (PIBITI). Algoritmos Inteligentes para Avaliação de Coerência e Coesão Textual em Atividades Escritas de Estudantes


### Contexto e Justificativa

A avaliação de coerência e coesão textual costuma ser feita manualmente, o que torna o processo lento, subjetivo e difícil de aplicar em grande escala. Para que algoritmos inteligentes consigam analisar esses aspectos do texto, é necessário primeiro que as produções escritas estejam digitalizadas com boa precisão — e é aí que entra este projeto.

O objetivo deste sistema, é atuar no reconhecimento de texto manuscrito, ele recebe imagens de atividades manuscritas de estudantes e as converte em texto digital de alta fidelidade, servindo de base para que os módulos de avaliação de coerência e coesão possam operar sem ruídos que comprometeriam a análise linguística.

### Objetivo Geral

Desenvolver e otimizar algoritmos de reconhecimento de texto manuscrito em português brasileiro, garantindo uma digitalização precisa das produções escritas de estudantes para viabilizar a posterior avaliação automatizada de coerência e coesão textual.

### Principais Frentes de Trabalho

- Revisão do estado da arte em reconhecimento de manuscritos (HTR), com foco em arquiteturas de deep learning.
- Técnicas de pré-processamento de imagem (binarização, correção de inclinação, remoção de ruído) para melhorar a qualidade das amostras antes do reconhecimento.
- Construção e anotação de um corpus de produções manuscritas de estudantes em português.
- Implementação e adaptação de modelos de HTR para lidar com a variabilidade caligráfica do português brasileiro.
- Avaliação sistemática de desempenho usando métricas como CER (Character Error Rate) e WER (Word Error Rate).
- Estruturação da saída do sistema em formato adequado para consumo pelo módulo de avaliação de coerência e coesão.


## Estrutura de pastas do Projeto

```
Projeto-PIBITI---Reconhecimento-de-Texto-Manuscrito/
│
├── data/                       # Dados utilizados pelo sistema
│   ├── raw/                    # Imagens manuscritas originais (entrada)
│   ├── processed/              # Imagens após pré-processamento
│   └── annotations/            # Textos de referência (Ground Truth) para avaliação
│
├── docs/                       # Documentação adicional do projeto
│
├── Include/                    # Arquivos de inclusão do ambiente virtual (gerado automaticamente)
│
├── notebooks/                  # Notebooks Jupyter para experimentação e testes exploratórios
│
├── src/                        # Código-fonte principal do sistema
│   ├── preprocessing/          # Módulo de pré-processamento de imagem
│   │   └── image_preprocessing.py
│   ├── model/                  # Módulo do modelo de reconhecimento (HTR)
│   │   └── htr_model.py
│   ├── inference/               # Módulo de inferência (uso do modelo em produção)
│   ├── evaluation/             # Módulo de avaliação de desempenho (métricas CER/WER)
│   │   └── metrics.py
│   └── pipeline.py             # Script principal que orquestra o pipeline completo
│
├── venv/                       # Ambiente virtual Python (não versionado no Git)
│
├── app.py                      # Interface web do sistema (Streamlit)
├── requirements.txt            # Dependências do projeto
├── .gitignore                  # Arquivos/pastas ignorados pelo controle de versão
└── README.md                   # Este arquivo
```

### Descrição dos módulos principais

- `preprocessing/image_preprocessing.py`: binariza a imagem e remove ruído antes do reconhecimento.
- `model/htr_model.py`: carrega o modelo TrOCR (Hugging Face) e reconhece o texto da imagem.
- `evaluation/metrics.py`: calcula CER e WER comparando o texto reconhecido com o texto de referência.
- `pipeline.py`: roda o fluxo completo (pré-processamento, reconhecimento e avaliação) via terminal.
- `app.py`: interface web em Streamlit para upload de imagem e visualização do resultado.

As pastas `venv/`, `Include/` e `__pycache__/` são geradas automaticamente pelo Python e não fazem parte do código-fonte.

## Como Rodar o Projeto

Ativar o ambiente virtual (Windows):
```bash
.\venv\Scripts\Activate.ps1
```

Instalar as dependências:
```bash
pip install -r requirements.txt
```

Rodar pela interface web:
```bash
streamlit run app.py
```

Ou rodar direto pelo terminal (dentro da pasta `src`):
```bash
cd src
python pipeline.py
```

Observação: o projeto usa `tokenizers==0.21.4` e `transformers==4.46.3`, versões compatíveis com Python 3.13.

## Arquitetura do Sistema

O sistema segue um pipeline sequencial, do upload da imagem até a saída do texto avaliado:

```
Upload da imagem manuscrita
        │
        ▼
Pré-processamento (binarização, remoção de ruído)
        │
        ▼
Segmentação (linhas, palavras, caracteres)
        │
        ▼
Modelo de HTR (TrOCR — microsoft/trocr-base-handwritten)
        │
        ▼
Pós-processamento (formatação da saída)
        │
        ▼
Avaliação (CER / WER) e exibição do resultado
```

Cada etapa é implementada como um módulo independente dentro de `src/`, o que permite testar, ajustar ou substituir cada parte do pipeline isoladamente (por exemplo, trocar o modelo de HTR sem alterar o pré-processamento).


## Como Usar

### Via linha de comando (`pipeline.py`)

Executa o pipeline completo (pré-processamento → reconhecimento → avaliação) sobre a imagem definida em `data/raw/exemplo.png`:

```bash
cd src
python pipeline.py
```

Saída esperada no terminal:
```
Texto reconhecido:
<texto identificado pelo modelo>

Avaliação:
{'WER': ..., 'CER': ...}
```

### Via interface web (`app.py`)

Interface interativa construída com Streamlit, que permite enviar qualquer imagem manuscrita e visualizar o resultado em tempo real.

```bash
streamlit run app.py
```

Isso abre automaticamente uma aba no navegador (geralmente em `http://localhost:8501`), onde é possível:

1. Fazer upload de uma imagem manuscrita (`.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.gif`).
2. Opcionalmente, inserir o texto de referência para calcular CER/WER automaticamente.
3. Clicar em **"Reconhecer texto"** e visualizar o resultado.

## Resultados Preliminares (Baseline)

| Imagem | Texto Reconhecido | WER | CER |
|---|---|---|---|
| `exemplo.png` | *(depende da amostra testada)* | 1.0 | ~0.86 |

Esses resultados representam o desempenho do modelo pré-treinado em inglês (`trocr-base-handwritten`) aplicado diretamente a manuscritos em português, sem qualquer ajuste — servindo como ponto de comparação para as próximas etapas de adaptação do modelo ao idioma.

## Próximos Passos

- [ ] Testar variações de pré-processamento (com e sem binarização) e comparar o impacto no CER/WER.
- [ ] Construir um conjunto de teste maior (5–10 imagens) para obter métricas médias mais confiáveis.
- [ ] Avaliar fine-tuning ou adaptação do modelo para português brasileiro.
- [ ] Testes de usabilidade da interface com usuários reais.
- [ ] Documentar plano de implantação em ambiente de produção.
