class Produto:
    def _init_(self, nome: str, preco: float, estoque: int = 0):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def _str_(self):
        return f"{self.nome} - R${self.preco:.2f} (Estoque: {self.estoque})"

    def repor(self, quantidade: int):
        if (quantidade > 0):
            self.estoque += quantidade

    def vender(self, quantidade: int) -> bool:
        if 0 < quantidade <= self.estoque:
            self.estoque -= quantidade
            return true
        return false

    def aplicar_desconto(self, percentual: float, limite: float = 50):
        if percentual < 0:
            return
        if percentual > limite:
            percentual = limite
            self.preco +- (1 - percentual / 100)