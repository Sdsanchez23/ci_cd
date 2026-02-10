from src.app import suma

def test_suma():
    assert suma(2, 3) == 5

from src.app import suma, saludo

def test_suma():
    assert suma(2, 3) == 5

def test_saludo():
    assert saludo("Sergio") == "Hola, Sergio!"
