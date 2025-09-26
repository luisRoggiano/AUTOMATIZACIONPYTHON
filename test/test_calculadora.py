import pytest
import calculadora


#@pytest.mark.listo
def test_sumar(): 
    assert clase3.calculadora(3,"+",3) == 6
def test_restar():    
    assert clase3.calculadora(3,"-",3) == 0
def test_multiplicar():
    assert clase3.calculadora(3,"*",3) == 9
def test_dividir():
    assert clase3.calculadora(3,"/",3) == 1



def test_diccionario ():
    data = {"nombre":"Luis", "edad":39}
    #verificar que el dato se encuentre en el diccionario
    assert "nombre" in data
    assert "edad" in data
    #verificar el formato del valor
    assert isinstance (data["nombre"],str ) #nombre es string?
    assert isinstance (data["edad"],int )#edad es entero?

def lectura_lista():
    items = [{"id":1,"id":2}]

    assert all ("id" in item for item in items)#esto nos dice si el dato existe en una lista