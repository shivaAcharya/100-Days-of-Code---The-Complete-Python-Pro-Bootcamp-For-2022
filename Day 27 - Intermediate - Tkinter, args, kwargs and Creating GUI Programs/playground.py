def calculate(n, **kwargs):
    # Here kwarg is a dictionary
    # for k, v in kwargs.items():   # If needed to access keys and values

    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n


print(calculate(2, add=5, multiply=10))
