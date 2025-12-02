# decorator.py

from functools import wraps

# Словник, де зберігається статистика викликів
calls_stats = {}

def count_same_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))  # ключ – аргументи

        if key not in calls_stats:
            calls_stats[key] = 0

        calls_stats[key] += 1

        print(f"Функцію '{func.__name__}' викликали з аргументами {key} – {calls_stats[key]} раз(и)")

        return func(*args, **kwargs)

    return wrapper
