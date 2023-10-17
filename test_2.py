import logging
import time

# Настройка логгирования.
# Если в программе более одного логирующих декораторов одного уровня,
# то в формат необходимо добавить %(funcName)s для того, чтобы различать из какого декоратора идёт запись.
logging.basicConfig(level=logging.INFO, filename="cache.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s ")

# словарь {имя функции : число вызовов до след исполнения}
# он нужен для того, чтобы для каждой функции отдельно отслеживать число вызовов
info_logging_dict = {}


def decorator_log(times_before_execution=3):
    def inner_decorator_log(func):
        def wrapper(*args, **kwargs):
            name = func.__name__
            # если функция не вызывалась ранее,
            # то заводим запись в словаре {name : times_before_execution}
            if name not in info_logging_dict:
                info_logging_dict[name] = times_before_execution

            # если функция вызывалась ранее,
            # то смотрим в словарь и если значение по ключу имени функции > 0 - не логируем
            # иначе - логируем
            if info_logging_dict[name] > 0:
                info_logging_dict[name] -= 1
                return func(*args, **kwargs)
            else:
                info_logging_dict[name] = times_before_execution
                start_time = time.time()
                n = func(*args, **kwargs)
                end_time = time.time()
                elapsed_time = end_time - start_time
                logging.info(f'Function "{func.__name__}" returned {n}.\n'
                             f'{" " * 28} Args: {args}. Kwargs: {kwargs}.\n'
                             f'{" " * 28} Elapsed time is {elapsed_time} seconds')
                return n
        return wrapper
    return inner_decorator_log


# decorator_log принимает 1 аргумент типа int - количество вызовов до логгировния
@decorator_log()
def function(n):
    res = 0
    for i in range(n):
        res += i
    return res


if __name__ == '__main__':
    while True:
        input()
        print(function(100000))