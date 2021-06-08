name = "Виктор Андреевич"
mid_name = ""
balance = 1000
text = """Уважаемый""" + " " + name + " " + mid_name + """, баланс вашего кошелька составляет""" + " " + str(balance) + """грн"""
print(text)

text2 = """Уважаемый {0} {1}, баланс вашего кошелька составляет {2}грн.""".format(name, mid_name, balance)
# name = 0
# mid_name = 1
# balance = 2
print(text2)

text3 = """Уважаемый {name} {mid_name}, баланс вашего кошелька составляет {balance}грн.""".format(name=name, mid_name=mid_name, balance=balance) 