from produto import Produto

def main():
    produto1 = Produto("Teclado mecanico", 350, estoque=10)
    produto2 = Produto("Mouse game", 150, estoque=20)

    print("Lista de Produtos")
    print(produto1)
    print(produto2)

    print("\nVendendo 5 teclados...")
    if produto1.vender(2):
        print("Venda realizada com sucesso!")
    else:
        print("Estoque insuficiente.")

if _name_ == "_main_":
    main()