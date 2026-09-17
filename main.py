from funciones.triangulo import leerBaseAltura, calcularArea, mostrarArea
from funciones.pago_semanal import leerHorasTarifa, calcularPago, mostrarPago
from funciones.conversion_tiempo import leerSegundos, convertirTiempo, mostrarTiempo

def main():
    #triangulo
    leerBaseAltura()
    calcularArea()
    mostrarArea()
    
    #pago semanal
    leerHorasTarifa()
    calcularPago()
    mostrarPago()
    
    #conversión de tiempo
    leerSegundos()
    convertirTiempo()
    mostrarTiempo()

if __name__ == "__main__":
    main()