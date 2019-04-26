# Решатель квадратных уравнений

Получает коэффициенты квадратного уравнения и возвращает корни

# Как использовать

def get_roots(a,b,c) - функция возвращающая корни квадратного уравнения
аргумент a - коэффициент x^2
аргумент b - коэффициент x^1
аргумент c - коэффициент x^0

результат функции кортеж из двух корней уравнения root1, root2
если корень один, то второй корень равен None
если уравнение не имеет корней, то результат None, None

Пример:

``` {.sourceCode .python}
>>> from quadratic_equation import get_roots

>>> root1, root2 = get_roots(1, 1, -6)
-3.0 2.0

>>> root1, root2 = get_roots(1, -2, 1)
1.0 None

>>> root1, root2 = get_roots(1, 2, 3)
None None
```
# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
