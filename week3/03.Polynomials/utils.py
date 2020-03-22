
def validate_polynomial(polynomial):
    if type(polynomial) is not str:
        raise TypeError("Polynomial must be a string")
    if polynomial == '':
        raise ValueError("Polynomial cannot be an empty string")
    if "-" in polynomial:
        raise ValueError("Polynomial shouldn't contain minuses")


def simplify_polynomial(polynomial):
    polynomial = polynomial.replace(" ", "")
    return polynomial.replace("*", "")
