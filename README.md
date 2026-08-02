
# Reconhecimento de Texto Manuscrito (PIBITI)

Sistema de reconhecimento de texto manuscrito (HTR) em português brasileiro, desenvolvido como parte do plano de trabalho de Iniciação em Desenvolvimento Tecnológico e Inovação (PIBITI), integrado ao projeto principal de avaliação automatizada de coerência e coesão textual em atividades escritas de estudantes.

## Sobre o Projeto

### Contexto e Justificativa

A avaliação de coerência e coesão textual costuma ser feita manualmente, o que torna o processo lento, subjetivo e difícil de aplicar em grande escala. Para que algoritmos inteligentes consigam analisar esses aspectos do texto, é necessário primeiro que as produções escritas estejam digitalizadas com boa precisão — e é aí que entra este projeto.

Diferente do OCR tradicional (eficaz para textos impressos), o reconhecimento de **manuscritos** é mais desafiador, especialmente em português brasileiro, devido à grande variação de caligrafia, à escrita cursiva e a particularidades regionais. Modelos de deep learning (como CNNs e RNNs) vêm avançando bastante nessa área, mas ainda há poucos datasets e soluções otimizadas especificamente para o português.

Este sistema atua como uma etapa habilitadora dentro do projeto maior: ele recebe imagens de atividades manuscritas de estudantes e as converte em texto digital de alta fidelidade, servindo de base para que os módulos de avaliação de coerência e coesão possam operar sem ruídos que comprometeriam a análise linguística.

### Objetivo Geral

Desenvolver e otimizar algoritmos de reconhecimento de texto manuscrito em português brasileiro, garantindo uma digitalização precisa das produções escritas de estudantes para viabilizar a posterior avaliação automatizada de coerência e coesão textual.

### Principais Frentes de Trabalho

- Revisão do estado da arte em reconhecimento de manuscritos (HTR), com foco em arquiteturas de deep learning.
- Técnicas de pré-processamento de imagem (binarização, correção de inclinação, remoção de ruído) para melhorar a qualidade das amostras antes do reconhecimento.
- Construção e anotação de um corpus de produções manuscritas de estudantes em português.
- Implementação e adaptação de modelos de HTR para lidar com a variabilidade caligráfica do português brasileiro.
- Avaliação sistemática de desempenho usando métricas como CER (Character Error Rate) e WER (Word Error Rate).
- Estruturação da saída do sistema em formato adequado para consumo pelo módulo de avaliação de coerência e coesão.

### Impacto Esperado

Além de viabilizar a análise automatizada de coerência e coesão, a digitalização precisa de atividades manuscritas contribui para a preservação de acervos educacionais, otimiza o tempo de professores na correção de atividades, favorece a inclusão digital (ex: conversão para leitores de tela) e ajuda a preencher a lacuna de pesquisas e datasets voltados ao português brasileiro nessa área.

## Estrutura do Projeto

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

| Módulo | Responsabilidade |
|---|---|
| `preprocessing/image_preprocessing.py` | Binarização, normalização e remoção de ruído das imagens manuscritas antes do reconhecimento |
| `model/htr_model.py` | Carrega o modelo de reconhecimento de texto manuscrito (TrOCR, Hugging Face) e realiza a predição do texto a partir da imagem |
| `evaluation/metrics.py` | Calcula as métricas de avaliação de desempenho — Character Error Rate (CER) e Word Error Rate (WER) — comparando o texto reconhecido com o texto de referência |
| `pipeline.py` | Script que integra pré-processamento, reconhecimento e avaliação em um fluxo único, via linha de comando |
| `app.py` | Interface web (Streamlit) que permite ao usuário enviar uma imagem manuscrita e visualizar o texto reconhecido e as métricas de avaliação |

> ⚠️ **Nota:** as pastas `venv/`, `Include/`, `__pycache__/` são geradas automaticamente pelo ambiente Python e não fazem parte do código-fonte propriamente dito — normalmente ficam listadas no `.gitignore` e não são versionadas no repositório.

---

## Guia Rápido: Como Rodar o Projeto

Passo a passo completo, do zero, para colocar o sistema em execução:

### 1. Ativar o ambiente virtual

Na raiz do projeto, abra o terminal e rode:

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

Se der erro de permissão:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Você vai saber que funcionou quando aparecer `(venv)` no início da linha do terminal.

### 2. Instalar as dependências (só na primeira vez, ou se algo mudou)

```bash
pip install -r requirements.txt
```

### 3. Escolher como rodar

**Opção A — Interface web (recomendado para uso geral):**

Rode a partir da **raiz do projeto**:
```bash
streamlit run app.py
```
Isso abre uma aba no navegador (`http://localhost:8501`) onde você sobe uma imagem manuscrita e vê o resultado na hora.

**Opção B — Linha de comando (para testes rápidos com uma imagem fixa):**

Entre na pasta `src` primeiro:
```bash
cd src
python pipeline.py
```
Isso processa a imagem definida em `data/raw/exemplo.png` e imprime o resultado direto no terminal.

### Resumo dos comandos (interface web)

```bash
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

### Resumo dos comandos (linha de comando)

```bash
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd src
python pipeline.py
```

## Instalação e Configuração do Ambiente

### Pré-requisitos

- Python 3.13
- Git (opcional, para clonar o repositório)

### 1. Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```
Se aparecer erro de permissão, rode antes:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

> ⚠️ **Nota sobre compatibilidade (Python 3.13):** as bibliotecas `tokenizers` e `transformers` precisam ser instaladas em versões específicas para evitar erros de build no Python 3.13 (o pacote `tokenizers` só tem binários pré-compilados para essa versão do Python a partir da release 0.20.3). As versões testadas e funcionais neste projeto são:
> ```
> tokenizers==0.21.4
> transformers==4.46.3
> ```
> Instale o `tokenizers` **antes** do `transformers`, nessa ordem, para evitar que o pip substitua a versão automaticamente.

### 3. Preparar os dados de entrada

Crie (se ainda não existirem) as subpastas de dados e adicione uma imagem manuscrita de teste:

```
data/raw/exemplo.png            # imagem manuscrita a ser reconhecida
data/annotations/exemplo.txt    # texto real correspondente (Ground Truth)
```

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

> **Observação técnica:** o modelo atual (`trocr-base-handwritten`) foi treinado em inglês (dataset IAM). Por isso, o desempenho em manuscritos de português brasileiro serve como *baseline* inicial do projeto — resultados de CER/WER altos nessa fase são esperados e servem como ponto de partida para a etapa de adaptação/ajuste do modelo ao português.

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
