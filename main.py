from Sis_vendas.produto import Produto
from Sis_vendas.venda import Venda


def formatar_moeda(valor):
    """Formata um valor para o padrão brasileiro de moeda."""
    return f"R$ {valor:.2f}"


def exibir_produtos(produtos):
    """Exibe a lista de produtos e seus dados."""
    print("\n===== PRODUTOS =====")
    for produto in produtos:
        print(f"\n{produto.descricao}")
        print(f"Preço: {formatar_moeda(produto.preco_unitario)}")
        print(f"Estoque: {produto.estoque}")


def exibir_itens_venda(venda):
    """Exibe os itens da venda."""
    print("\n===== ITENS DA VENDA =====")
    if not venda.itens:
        print("Nenhum item na venda.")
        return
    
    for item in venda.itens:
        plural = "unidade" if item.quantidade == 1 else "unidades"
        print(f"{item.produto.descricao} | {item.quantidade} {plural} | {formatar_moeda(item.calcular_subtotal())}")
    
    print(f"\nTOTAL: {formatar_moeda(venda.valor_total)}")


def exibir_estoque_final(produtos):
    """Exibe o estoque final de cada produto."""
    print("\n===== ESTOQUE APÓS VENDA =====")
    for produto in produtos:
        print(f"{produto.descricao}: {produto.estoque}")


def main():
    print("\n" + "="*50)
    print("SISTEMA DE VENDAS - TESTES")
    print("="*50)
    
    # Criando os produtos
    teclado = Produto("Teclado", 100.00, 10)
    mouse = Produto("Mouse", 50.00, 20)
    monitor = Produto("Monitor", 800.00, 5)
    
    produtos = [teclado, mouse, monitor]
    
    exibir_produtos(produtos)
    
    # Criando uma venda
    venda = Venda()
    
    print("\n===== CRIANDO VENDA =====")
    
    # TESTE 1: Adicionar 2 Teclados
    print("\nAdicionando 2 Teclados...")
    if venda.adicionar_item(teclado, 2):
        print("Adicionado com sucesso.")
    else:
        print("Erro ao adicionar.")
    
    # TESTE 2: Adicionar 3 Mouses
    print("\nAdicionando 3 Mouses...")
    if venda.adicionar_item(mouse, 3):
        print("Adicionado com sucesso.")
    else:
        print("Erro ao adicionar.")
    
    # TESTE 3: Adicionar 1 Monitor
    print("\nAdicionando 1 Monitor...")
    if venda.adicionar_item(monitor, 1):
        print("Adicionado com sucesso.")
    else:
        print("Erro ao adicionar.")
    
    # Exibir itens da venda
    exibir_itens_venda(venda)
    
    # Exibir estoque após venda
    exibir_estoque_final(produtos)
    
    # TESTE 4: Tentar adicionar mais produtos que o estoque
    print("\n===== TESTE DE ESTOQUE INSUFICIENTE =====")
    print("\nTentando adicionar 20 Monitores...")
    if venda.adicionar_item(monitor, 20):
        print("Adicionado com sucesso.")
    else:
        print("Estoque insuficiente.")
    
    # TESTE 5: Remover um item
    print("\n===== REMOVENDO ITEM =====")
    print("\nRemovendo Monitor...")
    if venda.remover_item(monitor):
        print("Monitor removido com sucesso.")
        print(f"\nNovo total: {formatar_moeda(venda.valor_total)}")
        print(f"Estoque do Monitor: {monitor.estoque}")
    else:
        print("Monitor não encontrado na venda.")
    
    # TESTE 6: Tentar remover um produto que não está na venda
    print("\n===== TESTE: REMOVER PRODUTO NÃO PRESENTE =====")
    print("\nTentando remover Monitor novamente...")
    if venda.remover_item(monitor):
        print("Monitor removido com sucesso.")
    else:
        print("Monitor não está na venda.")
    
    # Exibir estado final
    print("\n===== ESTADO FINAL =====")
    exibir_itens_venda(venda)
    exibir_estoque_final(produtos)
    
    print("\n" + "="*50)
    print("FIM DOS TESTES")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
