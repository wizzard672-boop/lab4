
import threading
from functools import wraps

class TimeoutError(Exception):
    """Исключение, выбрасываемое при превышении таймаута."""
    pass

def timeout(seconds: int):
    """
    Декоратор, ограничивающий время выполнения функции через потоки.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = [None]
            exception = [None]
            finished = [False]
            
            def target():
                """Целевая функция для отдельного потока."""
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    exception[0] = e
                finally:
                    finished[0] = True
            
            thread = threading.Thread(target=target)
            thread.daemon = True
            thread.start()
            thread.join(seconds)
            
            if not finished[0]:
                raise TimeoutError(f"Превышен лимит времени: {seconds} сек.")
            
            if exception[0] is not None:
                raise exception[0]
                
            return result[0]
            
        return wrapper
    return decorator


# Пример использования
if __name__ == "__main__":
    import time
    
    @timeout(5)
    def long_task():
        print("Долгая задача...")
        time.sleep(5)
        return "Готово"
    
    try:
        print(long_task())
    except TimeoutError as e:
        print(f" {e}")