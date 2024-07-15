import pytest
from src.sopa import crear_sopaLetras, colocar_horizontal, colocar_vertical, colocar_diagonal_positiva, colocar_diagonal_negativa, llenar_espacios_vacios

# Objetivo: Verificar que la función crear_sopa lance un ValueError si alguna de las palabras es más larga que el tamaño de la sopa.
def test_crear_sopaLetras_tamano_insuficiente():
    with pytest.raises(ValueError):
        crear_sopaLetras(["palabra", "demasiadoLarga"])
#-------------------------------------------------------------------------------------#
def test_colocar_horizontal():
    sopa = [[' ' for _ in range(10)] for _ in range(10)]
    assert colocar_horizontal(sopa, "HORIZON")
#-------------------------------------------------------------------------------------#
def test_colocar_vertical():
    sopa = [[' ' for _ in range(10)] for _ in range(10)]
    assert colocar_vertical(sopa, "VERT")
#-------------------------------------------------------------------------------------#
def test_colocar_diagonal_positiva():
    sopa = [[' ' for _ in range(10)] for _ in range(10)]
    assert colocar_diagonal_positiva(sopa, "DIAGPOS")
#-------------------------------------------------------------------------------------#
def test_colocar_diagonal_negativa():
    sopa = [[' ' for _ in range(10)] for _ in range(10)]
    assert colocar_diagonal_negativa(sopa, "DIAGNEG")
#-------------------------------------------------------------------------------------#
def test_llenar_espacios_vacios():
    sopa = [[' ' for _ in range(10)] for _ in range(10)]
    llenar_espacios_vacios(sopa)
    assert all(all(cell != ' ' for cell in row) for row in sopa)
