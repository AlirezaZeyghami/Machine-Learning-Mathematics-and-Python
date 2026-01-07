# to take number of attributes
attributes_num = int(input("Attributes Number: "))


# validation and settle entrance of Ali's fiance
while True:

    attributes_f = input("Enter female attributes: ").split()

    if len(attributes_f) == attributes_num:
        fiance_attributes = set(attributes_f)
        break

    else:
        print("Nums count or format is invalid, enter again!")


# validation and settle entrance of Ali
while True:

    attributes_a = input("Enter male attributes: ").split()

    if len(attributes_a) == attributes_num:
        ali_attributes = set(attributes_a)
        break

    else:
        print("Nums count or format is invalid, enter again!")


# intersection and utilizing
a_f_intersection = len(fiance_attributes & ali_attributes)


# check condition of understanding between Ali and his fiance
def f_n_intersection():

    if (attributes_num / 2) < a_f_intersection:
        print("YES")

    else:
        print("NO")


# run function of check
if __name__ == "__main__":

    f_n_intersection()
