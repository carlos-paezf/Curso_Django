class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro'] = {}
        # else:
        self.carro = carro

    def add_product(self, product):
        if (str(product.id) not in self.carro.keys()):
            self.carro[product.id] = {
                'product_id': product.id,
                'name': product.nombre,
                'price': str(product.precio),
                'amount': 1,
                'image': product.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(product.id):
                    value['amount'] += 1
                    break
        self.save_session()

    def save_session(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def delete_product(self, product):
        product.id = str(product.id)
        if product.id in self.carro:
            del self.carro[product.id]
            self.save_session()

    def substract_units_product(self, product):
        for key, value in self.carro.items():
            if key == str(product.id):
                value['amount'] -= 1
                if value['amount'] < 1:
                    self.delete_product(product)
                break
        self.save_session()

    def clean_carro(self):
        self.session['carro'] = {}
        self.session.modified = True
