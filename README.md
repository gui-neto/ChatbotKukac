# CHATBOT KUKAC

Este projeto consiste em um Chatbot de Questionário Interativo desenvolvido em Python, utilizando o framework Streamlit. A aplicação oferece uma experiência interativa aos usuários, permitindo que eles respondam a um questionário e recebam feedback instantâneo. A estruturação inicial do projeto envolve a criação de um ambiente virtual Python, instalação de bibliotecas como Streamlit e configuração do projeto conforme a documentação.

## Funcionalidades Principais

### Leitura e Manipulação do Arquivo JSON

- Implementação de uma função para upload e leitura de um arquivo JSON contendo perguntas do questionário.
Criação de estruturas de dados para armazenar e acessar as perguntas e respostas na memória.

### Lógica do Chatbot para Processamento de Perguntas

- Desenvolvimento da lógica backend para gerenciar o fluxo de perguntas do questionário.
Implementação de uma função para avaliar as respostas do usuário em comparação com as respostas corretas.
Informação da pontuação ao usuário e inclusão dessa pontuação no arquivo JSON de saída.

### Comunicação com o Frontend

- Estabelecimento de um sistema de comunicação eficiente entre o backend e o frontend.
Garantia de que o backend possa enviar perguntas e receber respostas do frontend de maneira dinâmica.

### Geração do Arquivo JSON de Perguntas e Respostas

- Compilação de todas as perguntas e respostas em um novo arquivo JSON após a conclusão do questionário.
Implementação de uma funcionalidade que permite ao usuário baixar este arquivo diretamente da interface Streamlit.
