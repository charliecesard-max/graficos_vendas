try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

dias = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]
Estoque = [80, 100, 150, 130, 100, 150, 150]
plt.figure("Vendas de Carnes")
plt.plot(dias, Estoque, marker='o', color="red", label="Estoque (kg)")
plt.title("Vendas de Carnes")
plt.ylabel("Quantidade no estoque (kg)")
plt.xlabel("Dias da Semana")
plt.grid(True)
plt.legend()

Produtos = ["Arroz", "Feijão", "Carne", "Macarrão", "Óleo", "Açúcar", "Café"]
Vendas = [150, 200, 300, 250, 400, 100, 180]
plt.figure("Vendas de Produtos")
plt.bar(Produtos, Vendas, color="blue", label="Vendas")
plt.title("Vendas de Produtos")
plt.ylabel("Unidades Vendidas")
plt.xlabel("Produtos")
plt.grid(False)
plt.legend()

Categorias = ["Eletrônicos", "Roupas", "Alimentos", "Móveis", "Brinquedos"]
Vendas_Cat = [8000, 10000, 4000, 2000, 6000]
plt.figure("Vendas por Categoria")
plt.pie(Vendas_Cat, labels=Categorias, autopct='%1.1f%%', startangle=90)
plt.title("Vendas por Categoria")

Precos = [60, 70, 30, 40, 50, 80, 90, 20, 10, 100, 110, 120]
Quantidade = [100, 80, 60, 40, 20, 10, 5, 15, 25, 30, 35, 40]
plt.figure("Preço x Quantidade")
plt.scatter(Precos, Quantidade, color="purple", label="Produtos")
plt.title("Relação Preço x Quantidade Vendida")
plt.xlabel("Preço (R$)")
plt.ylabel("Quantidade Vendida")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
