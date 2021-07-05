
def driver_connection(ip, port):
    def decorator(func):
        def inner(doc):
            print(f"Connected to IP: {ip}:{port}")
            func(doc)
            print(f"Close connection...")
        return inner
    return decorator

