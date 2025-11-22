def conversorTemperatura(opcao, graus):
    """
    Converte temperatura entre Celsius e Fahrenheit
    
    Args:
        opcao (int): 1 para Celsius→Fahrenheit, 2 para Fahrenheit→Celsius
        graus (float): Valor da temperatura a ser convertida
    
    Returns:
        float: Temperatura convertida
    
    Examples:
    >>> conversorTemperatura(1, 0)
    32.0
    
    >>> conversorTemperatura(1, 100)
    212.0
    
    >>> conversorTemperatura(1, -40)
    -40.0
    
    >>> conversorTemperatura(2, 32)
    0.0
    
    >>> conversorTemperatura(2, 212)
    100.0
    
    >>> conversorTemperatura(2, 98.6)
    37.0
    """
    if opcao == 1:
        return (graus * 9/5) + 32
    elif opcao == 2:
        return (graus - 32) * 5/9
    else:
        return "Opção inválida! Use 1 (C→F) ou 2 (F→C)"
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
