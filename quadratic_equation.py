from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1, root2 = None, None

    if discriminant > 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
    elif discriminant == 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
    return root1, root2
