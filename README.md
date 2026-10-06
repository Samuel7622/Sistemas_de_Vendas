# Sistema de Vendas

Sistema de vendas desenvolvido em Python a partir de um diagrama UML para praticar Programação Orientada a Objetos.

## Descrição

Este projeto implementa um sistema simples de vendas com classes para gerenciar produtos, itens de venda e vendas completas. O sistema controla o estoque de produtos e calcula valores de vendas de forma didática e fácil de compreender.

## Classes

### Produto
- Guarda descrição, preço unitário e quantidade em estoque
- Controla entrada e saída do estoque através de métodos específicos
- Evita que o estoque fique negativo
- Métodos principais:
  - `decrementar_estoque()`: reduz a quantidade em estoque
  - `incrementar_estoque()`: aumenta a quantidade em estoque

### ItemVenda
- Representa um produto dentro de uma venda
- Armazena o produto, quantidade e valor unitário
- Calcula o subtotal (quantidade × valor unitário)
- Método principal:
  - `calcular_subtotal()`: retorna o valor total do item

### Venda
- Armazena os itens de uma venda em uma lista
- Controla a adição e remoção de produtos
- Calcula o valor total da venda
- Métodos principais:
  - `adicionar_item()`: adiciona um produto e decrementa o estoque
  - `remover_item()`: remove um produto e incrementa o estoque
  - `calcular_total()`: soma todos os subtotais

## Estrutura de Arquivos

```
Sistemas_de_Vendas/
│
├── sisvenda/
│   ├── __init__.py        # Arquivo que torna a pasta um pacote Python
│   ├── produto.py         # Classe Produto
│   ├── item_venda.py      # Classe ItemVenda
│   └── venda.py           # Classe Venda
│
├── main.py                # Arquivo com testes do sistema
└── README.md              # Este arquivo
```

## Como Executar

```bash
python main.py
```

O programa executará uma série de testes mostrando:
1. Produtos cadastrados com preços e estoques
2. Adição de itens na venda
3. Cálculo automático de subtotais e total
4. Atualização de estoques
5. Teste com estoque insuficiente
6. Remoção de itens e devolução ao estoque
7. Teste de remoção de item não existente

## Conceitos de Programação Orientada a Objetos Utilizados

- **Classes e Objetos**: Estrutura de dados com atributos e métodos
- **Encapsulamento**: Uso de atributos privados (`__atributo`) e acesso via `@property`
- **Associação**: Relacionamento entre Produto, ItemVenda e Venda
- **Métodos**: Funções que realizam operações nos objetos
- **Listas**: Armazenamento de múltiplos itens em uma venda
- **Importação de Módulos**: Organização do código em arquivos separados
- **Modularidade**: Cada classe em seu próprio arquivo

## Regras de Negócio Implementadas

1. O estoque nunca pode ficar negativo
2. Só é possível adicionar um item se houver estoque suficiente
3. Ao remover um item, a quantidade volta para o estoque
4. O total da venda é atualizado automaticamente
5. Cada item armazena o preço no momento da venda
6. A data da venda é registrada automaticamente

## Autor

Desenvolvido como trabalho de avaliação mensal de Programação Orientada a Objetos.
