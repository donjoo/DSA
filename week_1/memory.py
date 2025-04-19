import time

def leak_free_memory():
    while True:
        big_data = [1] * (10**6)  # 1 million integers
        # Used and forgotten: No global reference
        print(f"Created and discarded a large list")
        time.sleep(1)

leak_free_memory()
