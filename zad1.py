"""
Задача 1. Замыкание для получения простых чисел.
"""

def prime_generator():
    """
    Возвращает функцию-замыкание, которая при каждом вызове выдает 
    следующее простое число.
    """
    # Внешнее окружение (состояние замыкания)
    primes = []
    current = 1

    def is_prime(n: int) -> bool:
        """Проверяет, является ли число простым, используя кэш primes."""
        if n < 2:
            return False
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True

    def get_next_prime() -> int:
        """Вычисляет и возвращает следующее простое число."""
        nonlocal current
        current += 1
        while not is_prime(current):
            current += 1
        primes.append(current)
        return current

    return get_next_prime


# Пример использования (для самостоятельного запуска)
if __name__ == "__main__":
    next_prime = prime_generator()
    print("Первые 10 простых чисел:")
    for i in range(10):
        print(f"{i+1}: {next_prime()}")