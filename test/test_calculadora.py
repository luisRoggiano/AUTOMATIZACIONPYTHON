import pytest
import clase4

def test_sumar():
    assert clase4.calculadora(float(3),"*",float(3)) == 9
