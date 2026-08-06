# print(0.1 + 0.2 == 0.3)
# print(0.1 + 0.2)

# from decimal import Decimal

# print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
# print(Decimal("0.1") + Decimal("0.2"))

# from decimal import Decimal, getcontext

# getcontext().prec = 6
# print(Decimal("1") / Decimal("7"))

# getcontext().prec = 8
# print(Decimal("1") / Decimal("7"))

from decimal import Decimal, getcontext

getcontext().prec = 6
print(Decimal("233") / Decimal("7"))
