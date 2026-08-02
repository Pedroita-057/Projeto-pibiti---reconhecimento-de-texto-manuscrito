# Reconhecimento de Texto Manuscrito (PIBITI)

Este projeto faz parte do meu plano de trabalho do projeto de reconhecimento de texto manuscrito do PIBITI, ligado a um projeto maior sobre avaliação automática de coerência e coesão textual em atividades de estudantes. Antes de conseguir avaliar coerência e coesão de um texto, primeiro devemos ter acesso a um texto de formato digital. Como muitas atividades ainda são feitas à mão, o objetivo aqui é pegar imagens de textos manuscritos e transformar em texto digital, para depois esse texto poder ser analisado pelos outros módulos do projeto.

## Por que isso é importante

Hoje essa correção é feita manualmente pelo professor, o que demanda muito tempo, principalmente em turmas grandes. Reconhecer texto impresso já é uma tecnologia relativamente resolvida (OCR), mas reconhecer letra manuscrita ainda é bem mais difícil, porque cada pessoa escreve do seu jeito. Em português isso fica ainda mais complicado, porque não existem tantos modelos prontos e testados como existe para o inglês.

A ideia deste plano de trabalho é justamente tentar resolver essa etapa de digitalização, para servir de base para o restante do projeto.

## De forma geral, que o sistema faz

1. Recebe uma imagem com um texto escrito à mão.
2. Faz um tratamento na imagem (deixa em preto e branco, tira ruído).
3. Usa um modelo de reconhecimento de texto manuscrito (chamado TrOCR) para tentar ler o que está escrito.
4. Se o usuário informar o texto real da imagem, o sistema calcula o quanto o texto reconhecido está próximo do certo (usando as métricas CER e WER).

## Estrutura de pastas

```
data/            imagens usadas (originais, processadas e os textos de referência)
src/
  preprocessing/ tratamento da imagem antes do reconhecimento
  model/         carrega o modelo e reconhece o texto
  evaluation/    calcula CER e WER
  pipeline.py    roda tudo em sequência, pelo terminal
app.py           interface feita em Streamlit, para testar pelo navegador
requirements.txt lista das bibliotecas usadas
```

As pastas `venv/` e `__pycache__/` são criadas automaticamente pelo Python, não precisam ser mexidas.

## Como rodar

Ativar o ambiente virtual:
```
.\venv\Scripts\Activate.ps1
```

Instalar as bibliotecas necessárias:
```
pip install -r requirements.txt
```

Rodar pela interface:
```
streamlit run app.py
```

Ou rodar direto pelo terminal, sem interface (dentro da pasta `src`):
```
cd src
python pipeline.py
```

Obs: no meu computador, que usa Python 3.13, precisei instalar versões específicas do `tokenizers` e `transformers` (0.21.4 e 4.46.3) para não dar erro de instalação.

## Testes que fiz

Depois que o sistema ficou funcionando, pedi para duas pessoas testarem, cada uma enviando uma foto de um texto escrito à mão.

No primeiro teste, o sistema não reconheceu quase nada do texto certo.

No segundo teste, percebi um problema diferente: o modelo ficou repetindo a mesma palavra várias vezes na resposta, ao invés de tentar ler o restante do texto. Pesquisei sobre isso e descobri que dá pra configurar o modelo para penalizar repetições, usando os parâmetros `repetition_penalty` e `no_repeat_ngram_size`. Depois de adicionar isso na função que gera o texto, esse problema de repetição melhorou.

De modo geral, os resultados ainda não ficaram bons, mas isso já era esperado: o modelo usado foi treinado com textos em inglês, não em português, então ele erra bastante ao tentar ler manuscritos em português. Esse é o ponto de partida do projeto — a próxima etapa é justamente tentar melhorar esse reconhecimento para o nosso idioma.

## Implantação em ambiente de produção

Depois dos testes locais, coloquei o sistema no ar de verdade, usando o Streamlit Community Cloud (é gratuito e funciona direto com o código do GitHub, sem precisar reescrever nada).

Os passos que segui, resumindo:

Subi o projeto para um repositório no GitHub.
Criei uma conta no Streamlit Cloud e conectei ao repositório, apontando para o app.py.
Na primeira tentativa, o deploy deu erro. Fui corrigindo um por um, conforme os logs mostravam:
o opencv-python não funciona no ambiente da nuvem, precisei trocar para opencv-python-headless;
o arquivo requirements.txt, gerado automaticamente no meu computador, tinha versões de biblioteca que não existiam ou conflitavam entre si (numpy, huggingface_hub, tokenizers). Fui ajustando as versões até o pip conseguir instalar tudo sem conflito.
Depois de resolver as instalações, o app subiu e ficou acessível por um link público.

Com o sistema já publicado, testei de novo o reconhecimento de texto e os resultados continuaram fracos, do mesmo jeito que nos testes locais — o que reforça que o problema não é do ambiente, e sim do modelo em si, que não foi treinado em português.

## Próximos passos

- Testar mais imagens, com textos diferentes, para ter uma ideia melhor da taxa de erro.
- Ver se ajuda tirar a binarização da imagem antes de mandar pro modelo.
- Estudar como adaptar o modelo para reconhecer melhor o português.
- Continuar os testes de usabilidade da interface com mais pessoas.

parei no monitoramento