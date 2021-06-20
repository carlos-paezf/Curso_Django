def total_amount_carro(request):
    total = 0
    #if request.user.is_authenticated:
    for key, value in request.session['carro'].items():
        total += (float(value['price']))
    return {'total_amount_carro': total}
