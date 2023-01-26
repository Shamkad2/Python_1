from datetime import datetime as dt


def log_operation(data):
    time = dt.now().strftime('%D %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as f:
        f.write(f"{time}  Operation: {data}  ")


def log_data(data):
    with open('log.csv', 'a', encoding='utf-8') as f:
        f.write(f"Number: {data}  ")


def log_result(data):
    with open('log.csv', 'a', encoding='utf-8') as f:
        f.write(f"Result: {data}\n")
        f.write('-' * 50 + '\n')
