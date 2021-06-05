def derivative(f, x0=0):
    x = 1e8
    return round(f(x0 + x) - f(x0) / x, 3)
