# Projeto-pibit---reconhecimento-de-texto-manuscrito
Este projeto foca no reconhecimento de texto manuscrito (HTR) em português brasileiro aplicado a atividades educacionais, visando fornecer entrada textual de alta qualidade para sistemas de avaliação de coerência e coesão.

Problema:


Objetivo:
Objetivo Geral: Desenvolver e otimizar algoritmos de reconhecimento de texto manuscrito em língua portuguesa brasileira, utilizando técnicas avançadas de Inteligência Artificial, para garantir a digitalização precisa de produções escritas de estudantes, fornecendo uma base textual de alta qualidade para a posterior avaliação de coerência e coesão. Objetivos Específicos: Revisar o Estado da Arte em HTR: Realizar uma revisão aprofundada da literatura sobre reconhecimento de texto manuscrito, com foco em Redes Neurais Convolucionais (CNNs) e Redes Neurais Recorrentes (RNNs), identificando as arquiteturas mais eficazes e as tendências para o tratamento da variabilidade da escrita manual, especialmente em línguas com características similares ao português brasileiro. Desenvolver Técnicas de Pré-processamento Otimizadas: Explorar e implementar técnicas avançadas de pré-processamento de imagens (e.g., binarização adaptativa, normalização de inclinação e tamanho, remoção de ruídos) para maximizar a qualidade das amostras de escrita manual, minimizando artefatos que possam impactar negativamente o reconhecimento. Construir e Anotar Corpus de Produções Educacionais: Coletar, selecionar e criar um conjunto de dados representativo de produções escritas manuscritas de estudantes em português brasileiro, abrangendo diferentes níveis de ensino, estilos de escrita e tipos de atividades, e realizar a anotação precisa (Ground Truth) para treinamento e validação dos modelos de HTR. Implementar e Adaptar Modelos de HTR: Desenvolver e adaptar modelos de deep learning (CNNs, RNNs ou abordagens híbridas) para o reconhecimento de caracteres e palavras em manuscritos de Pt-Br, focando na robustez frente às variações caligráficas e ortográficas do idioma. Avaliar e Otimizar a Precisão da Digitalização: Avaliar rigorosamente o desempenho dos modelos de HTR desenvolvidos utilizando métricas como Character Error Rate (CER) e Word Error Rate (WER), e comparar com benchmarks existentes, realizando iterações de otimização para aprimorar a precisão e a eficiência da digitalização. Garantir Saída Preparada para Análise de Coerência e Coesão: Assegurar que o texto digitalizado pelos algoritmos de HTR seja fornecido em um formato limpo e estruturado, ideal para ser consumido pelos módulos de avaliação de coerência e coesão textual, preservando a pontuação e a estrutura frasal. Disseminar o Conhecimento e Resultados: Documentar o processo de desenvolvimento, os algoritmos empregados e os resultados obtidos, com o objetivo de produzir artigos científicos para submissão em periódicos e conferências de relevância em IA, PLN e educação.

Estado atuaL:

Seleção e Instalação das Ferramentas de Desenvolvimento de Software Necessárias

As ferramentas de desenvolvimento foram selecionadas considerando critérios como compatibilidade com técnicas de Inteligência Artificial e Deep Learning, amplo uso na comunidade científica, suporte ao reconhecimento de texto manuscrito (HTR), disponibilidade gratuita e facilidade de integração.

Foi adotada a linguagem Python (versão 3.10 ou superior), devido à sua ampla aplicação em pesquisas acadêmicas, simplicidade e grande ecossistema de bibliotecas voltadas à visão computacional e aprendizado profundo. Como ambiente de desenvolvimento, utilizou-se o Visual Studio Code, por oferecer suporte nativo ao Python, integração com Git e extensões que auxiliam no desenvolvimento e organização do código.

Para o desenvolvimento dos modelos de Inteligência Artificial, foram utilizados os frameworks PyTorch e Torchvision, amplamente empregados em pesquisas científicas. O processamento de imagens manuscritas foi realizado com as bibliotecas OpenCV e Pillow, enquanto o reconhecimento de texto manuscrito foi implementado com o uso da biblioteca Transformers, por meio do modelo TrOCR, reconhecido como estado da arte nessa área.

A avaliação de desempenho do sistema foi realizada com a biblioteca JiWER, utilizada para o cálculo das métricas CER e WER. O gerenciamento das dependências foi feito com pip, em conjunto com um ambiente virtual Python (venv), garantindo o isolamento do projeto. Para controle de versões e desenvolvimento colaborativo, foram utilizados Git e GitHub.

Após a instalação e configuração das ferramentas, o ambiente foi validado por meio da execução de testes de importação das principais bibliotecas, assegurando que o sistema estava pronto para o início do desenvolvimento do projeto de reconhecimento de texto manuscrito.

Configuração de um Ambiente de Desenvolvimento Colaborativo (GitHub)

O ambiente de desenvolvimento colaborativo foi configurado utilizando a plataforma GitHub, escolhida por sua ampla adoção na comunidade científica e de desenvolvimento de software, além de oferecer recursos eficientes para controle de versões, documentação e acompanhamento da evolução do projeto.

Inicialmente, foi criado um repositório remoto, que passou a centralizar o código-fonte e os arquivos do projeto. Esse repositório foi integrado ao ambiente local por meio do sistema de versionamento Git, permitindo o registro contínuo das alterações realizadas ao longo do desenvolvimento.

Foi definida uma estrutura inicial de diretórios, organizada para separar dados, código-fonte, notebooks e documentação, favorecendo a organização, manutenção e escalabilidade do projeto. Também foram configurados arquivos essenciais para o trabalho colaborativo, como o .gitignore, para evitar o versionamento de arquivos sensíveis ou desnecessários, o README.md, contendo a descrição do projeto e tecnologias utilizadas, e o requirements.txt, responsável pelo gerenciamento das dependências.

Além disso, adotou-se uma estratégia básica de branches, separando a versão estável do código das versões em desenvolvimento, o que contribui para maior controle e qualidade do projeto, mesmo em um cenário com poucos colaboradores. O uso de issues foi definido como mecanismo de planejamento, registro de atividades e acompanhamento da evolução do sistema.

Ao final dessa etapa, o projeto encontrava-se devidamente versionado, documentado e preparado para o desenvolvimento colaborativo e acadêmico, garantindo rastreabilidade, organização e boas práticas de engenharia de software.



