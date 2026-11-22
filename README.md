# RentSmart — Sistema de Orçamento de Locação

## 1. Sobre o projeto

O RentSmart é uma aplicação desenvolvida em Python para automatizar a elaboração de orçamentos de locação de imóveis da imobiliária fictícia R.M Imóveis.

O sistema permite selecionar diferentes tipos de imóveis, informar suas características e calcular automaticamente o valor mensal da locação, considerando adicionais, descontos e condições de pagamento da taxa contratual.

A aplicação possui uma interface gráfica que facilita a utilização e apresenta os resultados de maneira organizada.

## 2. Objetivo

O objetivo do projeto é facilitar o processo de elaboração de orçamentos de locação, reduzindo cálculos manuais e possíveis erros na aplicação das regras comerciais.

Também foi desenvolvido com a utilização dos conceitos de Programação Orientada a Objetos, organizando o código em classes, atributos e métodos.

## 3. Funcionalidades

O RentSmart possui as seguintes funcionalidades:

- Seleção entre apartamentos, casas e estúdios.
- Cálculo automático do aluguel mensal.
- Aplicação de adicionais por quantidade de quartos.
- Cálculo de vagas de garagem e estacionamento.
- Aplicação de desconto de 5% para apartamentos de clientes sem crianças.
- Cálculo da taxa contratual de R$ 2.000,00.
- Parcelamento da taxa contratual em até cinco vezes.
- Apresentação do resumo financeiro do orçamento.
- Geração de arquivo CSV com a projeção dos 12 meses de locação.

## 4. Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento da aplicação.
- **Tkinter:** biblioteca utilizada para criar a interface gráfica.
- **CSV:** recurso utilizado para gerar os relatórios financeiros.
- **Visual Studio Code:** ambiente utilizado para desenvolver o projeto.

## 5. Estrutura do projeto

```text
RentSmart/
│
├── models/
│   ├── __init__.py
│   ├── imovel.py
│   ├── apto.py
│   ├── casa.py
│   └── estudio.py
│
├── services/
│   ├── __init__.py
│   ├── orcamento.py
│   └── gerador_csv.py
│
├── ui/
│   ├── __init__.py
│   ├── componentes.py
│   ├── janela_principal.py
│   └── tela_orcamento.py
│
├── relatorios/
│
├── main.py
└── README.md
```

## 6. Regras de negócio

O sistema utiliza as seguintes regras para calcular os valores dos imóveis:

| Tipo de imóvel          |  Valor-base |
| ----------------------- | ----------: |
| Apartamento de 1 quarto |   R$ 700,00 |
| Casa de 1 quarto        |   R$ 900,00 |
| Estúdio                 | R$ 1.200,00 |

**Adicionais e condições comerciais:**

- Apartamento com dois quartos: adicional de R$ 200,00.
- Casa com dois quartos: adicional de R$ 250,00.
- Garagem para casas e apartamentos: adicional de R$ 300,00.
- Estúdio: pacote inicial de duas vagas por R$ 250,00.
- Vagas adicionais para estúdios: R$ 60,00 por vaga.
- Apartamentos de clientes sem crianças: desconto de 5% após os adicionais.
- Taxa contratual: R$ 2.000,00, com possibilidade de parcelamento em até cinco vezes.

## 7. Como executar o projeto

Para executar o RentSmart, é necessário ter o Python instalado no computador.

**Passo 1 — Obter os arquivos**

Baixe o projeto ou clone o repositório do GitHub.

**Passo 2 — Abrir a pasta**

Abra a pasta principal do RentSmart no Visual Studio Code.

**Passo 3 — Executar o sistema**

Abra o terminal na pasta principal e execute:

```bash
python main.py
```

No Windows, caso necessário, também é possível utilizar:

```bash
py main.py
```

**Passo 4 — Utilizar a aplicação**

Após a execução, a janela principal será aberta. Selecione a opção de novo orçamento, informe as características do imóvel e escolha a condição de parcelamento contratual.

O sistema realizará os cálculos e apresentará o resumo financeiro.

## 8. Geração de relatórios

Após calcular um orçamento, o usuário poderá selecionar a opção de gerar projeção CSV.

O arquivo será criado automaticamente dentro da pasta `relatorios`, com o nome:

`projecao_locacao.csv`

O documento apresenta a previsão dos pagamentos dos primeiros 12 meses, separando o aluguel mensal das parcelas da taxa contratual.

## 9. Programação Orientada a Objetos

Durante o desenvolvimento foram utilizados conceitos de Programação Orientada a Objetos, incluindo:

- **Classes e objetos:** representação dos imóveis e dos orçamentos.
- **Atributos:** armazenamento das características de cada imóvel.
- **Métodos:** realização dos cálculos e apresentação das informações.
- **Herança:** utilização de uma classe principal de imóvel para estruturar apartamentos, casas e estúdios.
- **Composição:** utilização de objetos de imóveis na elaboração dos orçamentos.

Essa organização permitiu separar as responsabilidades e facilitar a manutenção do código.

## 10. Considerações finais

O desenvolvimento do RentSmart permitiu aplicar conhecimentos de lógica de programação, pensamento algorítmico e Programação Orientada a Objetos na construção de uma aplicação funcional.

Com o sistema, foi possível automatizar os cálculos de locação, organizar as informações financeiras e gerar uma projeção dos pagamentos, contribuindo para tornar o processo de elaboração de orçamentos mais simples e organizado.

---

**Projeto acadêmico — Algorithmic Thinking & Introduction to Object-Oriented Programming.**
