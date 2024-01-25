# cosmetic_factory.py
from cosmetics.cosmetic_product import CosmeticProduct

class CosmeticFactory:
    def create_cosmetic_product(self, name, brand, price, quantity):
        return CosmeticProduct(name, brand, price, quantity)

# Пример использования фабрики:
if __name__ == "__main__":
    cosmetic_factory = CosmeticFactory()
    new_lipstick = cosmetic_factory.create_cosmetic_product("New Lipstick", "Revlon", 12.99, 40)

    print(new_lipstick)