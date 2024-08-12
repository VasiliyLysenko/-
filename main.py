import multiprocessing


class WarehouseManager:
    data = {}

    def process_request(self, request):
        prod_name = request[0]
        action = request[1]
        quantity = request[2]
        if prod_name in self.data:
            if action == 'receipt':
                self.data[prod_name] += quantity

            if action == 'shipment':
                if self.data[prod_name] < quantity:
                    print('Товара на складе недостаточно для отгрузки')
                else:
                    self.data[prod_name] -= quantity
        else:
            self.data[prod_name] = quantity
        return self.data
    def run(self, requests):
        with multiprocessing.Pool(processes=4) as pool:
            self.data = pool.map(self.process_request, requests)


manager = WarehouseManager()

req = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
if __name__ == '__main__':
    manager.run(req)
    print(manager.data)
