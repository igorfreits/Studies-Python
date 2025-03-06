# Aula 73
def sum(x, y):
    """
    Sum x and y
    :Parameter x: number 1
    :type x: int  or  float
    :parameter y: number 2
    :type y: int or float

    :return: The sum of x and y # A soma entre x e y
    :return type: int or float
    """
    return x+y


def multiplies(x, y, z=None):
    """multiplies x,y,z
    Devops pode omitir a variável z cao nao tenha necessidade de usar

    :Parameter x: number 1
    :type x: int  or  float
    :parameter y: number 2
    :type y: int or float
    :parameter z: number  3 (optional)
    :type z: int,float or None

    :return: The sum of x,y and z
    :return type: int or float 

    """
    if z:
        return x * y
    else:
        return x * y * z
