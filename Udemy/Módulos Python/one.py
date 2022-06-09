# aula 77

def sum(x: float, y: float) -> float:
    return x + y

"""Se o arquivo for o __main__ sera executado somente naquele scrypt"""
def main() -> None:
    print(f'\033[35m{__name__}\033[m')
    print(sum(30, 40))
    print(sum(10, 80))


if __name__ == '__main__':
    main()
