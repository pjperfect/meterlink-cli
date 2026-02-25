import time
from datetime import datetime

def log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        log_message = f"""
        _____LOG ENTRY_____
        Timestamp: {timestamp}
        Function: {func.__name__}
        time taken: {time_taken} seconds
        result: {result}
        ____________________
        """
        file_handle = open("log.txt", "a")
        file_handle.write(log_message)
        file_handle.close()
        return result
    return wrapper