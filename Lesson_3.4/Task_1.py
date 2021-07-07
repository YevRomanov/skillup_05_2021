#######################################Task 1#######################################
#
# 
def driver_connection(ip, port):
    def decorator(func):
        def inner(doc):
            print(f"Connected to IP: {ip}:{port}")
            func(doc)
            print(f"Close connection...")
        return inner
    return decorator

@driver_connection(ip="11.10.11.10", port="6699")
def hp(doc):
    print("I am HP printer")
    print(f'Printing: {doc}')
    
@driver_connection(ip="11.11.10.11", port=7744)
def canon(doc):
    print("I am Canon printer")
    print(f'Printing: {doc}')

hp('Test text')
canon('Test text_2')
