

def product(fracs):
    # complete this line with a reduce statement
    t = Fraction(reduce(lambda x, y: x * y, fracs))
    return t.numerator, t.denominator

