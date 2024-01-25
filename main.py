from cosmetics.cosmetic_product import CosmeticProduct
from cosmetics.cosmetic_factory import CosmeticFactory
from cosmetics.cosmetic_stock import StockObserver, CosmeticStock

if __name__ == "__main__":
    # Пример использования классов из пакета "cosmetics"
    lipstick = CosmeticProduct("Lipstick", "Maybelline", 10.99, 50)
    mascara = CosmeticProduct("Mascara", "L'Oreal", 8.99, 30)

    cosmetic_factory = CosmeticFactory()
    new_lipstick = cosmetic_factory.create_cosmetic_product("New Lipstick", "Revlon", 12.99, 40)

    cosmetic_stock = CosmeticStock()
    low_stock_observer = StockObserver(threshold=50)
    cosmetic_stock.add_observer(low_stock_observer)

    cosmetic_stock.add_product(lipstick)
    cosmetic_stock.add_product(mascara)
    cosmetic_stock.add_product(new_lipstick)
