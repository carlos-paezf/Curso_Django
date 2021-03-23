class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro'] = {}
        else:
            self.carro = Carro
    
    def add_product(self, product):
        if (str(product.id) not in self.carro.keys()):
            self.carro[product.id] = {
                'product_id': product.id, 
                'name': product.name, 
                'price': str(product.price), 
                'amount': 1, 
                'image': product.image.url
            }