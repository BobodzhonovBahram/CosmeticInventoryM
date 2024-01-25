# cosmetic_stock.py
from cosmetics.cosmetic_product import CosmeticProduct
from cosmetics.cosmetic_factory import CosmeticFactory

class Observer:
    def update(self, product):
        pass

class StockObserver(Observer):
    def __init__(self, threshold):
        self.threshold = threshold

    def update(self, product):
        if product.quantity < self.threshold:
            print(f"Low stock alert for {product.brand} {product.name}. Current quantity: {product.quantity}")

class CosmeticStock:
    def __init__(self):
        self.products = []
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def add_product(self, product):
        self.products.append(product)
        self.notify_observers(product)

    def notify_observers(self, product):
        for observer in self.observers:
            observer.update(product)

# Пример использования:
if __name__ == "__main__":
    cosmetic_stock = CosmeticStock()

    # Добавляем наблюдателя, который будет предупреждать о низком уровне запасов
    low_stock_observer = StockObserver(threshold=50)
    cosmetic_stock.add_observer(low_stock_observer)

    # Добавляем продукты на склад
    lipstick = CosmeticProduct("Lipstick", "Maybelline", 10.99, 45)
    mascara = CosmeticProduct("Mascara", "L'Oreal", 8.99, 30)

    cosmetic_stock.add_product(lipstick)
    cosmetic_stock.add_product(mascara)
