# Module "Sale"
# 6- Intra-package References
# 1:
# from ..customer import contact
# 2: related referencing (. means in the current dir. and .. means a level back (here:ecommerce))
# from ecommerce.customer import contact

print("sale module started.")


def calc_shipp():
    print("shipp")


def calc_shipping():
    print("shipping")


if __name__ == "__main__":
    print("sale is running as main.")