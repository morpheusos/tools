

def log_innit():
    global log_file
    global log_cache
    log_file = ""
    log_cache = []

def log(content):
    global log_file
    log_file += str(content) + "\n"

def log_print(cache=False):
    global log_file
    print(log_file)
    if cache:
        counter = 0
        for log in log_cache:
            print(counter)
            print(log)
            counter += 1

def log_dump():
    global log_file
    global log_cache
    log_cache.append(log_file)
    log_file = ""