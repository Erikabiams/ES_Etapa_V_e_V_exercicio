def calcular_multa(velocidade):
    """
    Calcula o valor da multa por excesso de velocidade
    
    Args:
        velocidade (float): Velocidade do veículo em km/h
    
    Returns:
        float: Valor da multa em R$ (0 se não houver infração)
    
    Examples:
    >>> calcular_multa(30)
    0.0
    
    >>> calcular_multa(60)
    0.0
    
    >>> calcular_multa(61)
    203.0
    
    >>> calcular_multa(85)
    275.0
    
    >>> calcular_multa(120)
    380.0
    
    >>> calcular_multa(-8)
    'Velocidade inválida!'
    
    >>> calcular_multa("cinco")
    'Velocidade inválida!'
    """
   
    if not isinstance(velocidade, (int, float)):
        return "Velocidade inválida!"
    
    if velocidade < 0:
        return "Velocidade inválida!"
    
    if velocidade > 60:
        excesso = velocidade - 60
        multa = 200 + (excesso * 3)
        return float(multa)  
        
    return 0.0  


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
