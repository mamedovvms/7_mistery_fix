from math import sqrt


def main():
    root1, root2 = get_roots(1, 1, -6)
    print(root1, root2)

    root1, root2 = get_roots(1, 2, 3)
    print(root1, root2)

def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1, root2 = None, None

    if discriminant > 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
    elif discriminant == 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
    return root1, root2


if __name__ == '__main__':
    main()
