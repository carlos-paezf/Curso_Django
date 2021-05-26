def total_amount_carro(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session['Carro'].items():
            total += (float(value['price']) * value['amount'])
    return {'total_amount_carro': total}
