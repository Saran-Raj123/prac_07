def main():
    print('total price of 3 items')
    price = input(">>> ").upper()
    while price != "100":
        if price == "100":
            price = float(input("price: "))
            price = 100 * 3
            print('total price of 3 items')
    price = input(">>> ").upper()
    while price != "35..56":
        if price == "35.56":
            price = float(input("price: "))
            price = 35.56 * 3
            print('total price of 3 items')
    while price != "3.24":
        if price == "3.24":
            price = float(input("price: "))
            price = 3.24 * 3
            print('total price of 3 items')

