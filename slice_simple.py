def slice_simple():
    texto = "Awesome"
    texto[:3].lower()
    texto[2:5].lower()
    texto[:4].lower()+texto[-3:]

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
