def _calc_electro(tiempo_uso, precio_kwh, consumo): 
    return tiempo_uso*precio_kwh*consumo
    

def sum_todos(usuario:dict):
    suma_total=0
    for electrodomestico in usuario:
        suma_total+=_calc_electro(electrodomestico.get('tiempo_uso'),0.000002,electrodomestico.get('consumo'))
        
    return suma_total