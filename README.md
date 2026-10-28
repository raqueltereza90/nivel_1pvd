# 🛒 PDV em Python

Este projeto foi desenvolvido como parte de um desafio de programação para praticar meus conhecimentos em Python. A ideia foi criar um sistema de Ponto de Venda (PDV) capaz de registrar compras, calcular descontos e apresentar um resumo das vendas realizadas.

Durante o desenvolvimento, trabalhei com regras de negócio, estruturas condicionais, laços de repetição e armazenamento de informações.

## 💻 Como funciona?

O programa recebe o valor da compra e a idade do cliente e calcula os descontos de acordo com as regras estabelecidas.

Na versão básica, o sistema oferece:
- Desconto de 20% para clientes com 65 anos ou mais.
- Desconto adicional de 10% quando o valor após o desconto por idade ultrapassa R$ 100,00.
- Registro de várias compras em uma única execução.
- Histórico das compras e resumo dos valores no final.

## ⭐ Versão bônus

Depois de desenvolver a versão básica, também implementei uma versão bônus para acrescentar novas funcionalidades ao sistema.

Nessa versão, adicionei:
- **Desconto por quantidade:** mais 5% de desconto para compras com mais de três itens.
- **Cupom de fidelidade:** mais 10% de desconto para clientes que utilizam o cupom `FIDELIDADE10`.
- **Salvamento do resumo:** gravação das informações em um arquivo chamado `resumo.txt`.

## 🛠️ Tecnologias e conceitos utilizados

- Python 3
- Variáveis e tipos de dados
- Entrada e saída de dados
- Estruturas condicionais (`if`, `elif` e `else`)
- Laços de repetição (`while True` e `for`)
- Controle de fluxo (`break` e `continue`)
- Listas e dicionários
- Adição de registros (`append`)
- Cálculos percentuais
- Validação de dados
- Manipulação de textos (`.strip()` e `.upper()`)
- Manipulação de arquivos (`open()`, `write()` e `close()`)
- Codificação de caracteres (`encoding="utf-8"`)

## ▶️ Como executar

Para executar o projeto, é necessário ter o Python 3 instalado.

**Versão básica:**

```bash
python3 pdv.py
```

**Versão bônus:**

```bash
python3 pdv_bonus.py
```

Os nomes dos arquivos nos comandos devem corresponder aos nomes utilizados no projeto.

## 📚 O que aprendi com esse projeto?

Esse desafio me ajudou a praticar a lógica de programação e a entender melhor como utilizar Python para resolver problemas do dia a dia.

Também pude explorar novas possibilidades na versão bônus, trabalhando com descontos adicionais e cupons promocionais. Além disso, aprendi a salvar informações em arquivos de texto (`.txt`) utilizando Python para registrar o resumo das compras realizadas.
Pretendo continuar desenvolvendo meus conhecimentos e aplicar o que aprendi em projetos cada vez mais completos.
