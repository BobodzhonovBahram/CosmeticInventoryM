class CosmeticProduct:
    def __init__(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.brand} {self.name} - ${self.price} - Quantity: {self.quantity}"

# Пример использования:
if __name__ == "__main__":
    lipstick = CosmeticProduct("Lipstick", "Maybelline", 10.99, 50)
    mascara = CosmeticProduct("Mascara", "L'Oreal", 8.99, 30)

    print(lipstick)
    print(mascara)

