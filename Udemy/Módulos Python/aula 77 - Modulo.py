"""if __name__ == "__main__"""
from one import sum

# É um código padrão que protege os usuários de invocar acidentalmente o script quando não pretendiam
"""Se o arquivo for o __main__ sera executado somente naquele scrypt"""
print(f'\033[35m{__name__}\033[m')
print(sum(10, 10))
