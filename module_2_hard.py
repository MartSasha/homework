import random
a = 3
b = 20
box_1 = random.randint(a, b)
print(box_1)
def password(box_2):
    right_password = ''
    for i in range(1, box_2):
        for j in range(2, box_2):
            if j <= i:
                continue
            if box_2 % (i + j) == 0:
                right_password += str(i) + str(j)
    return right_password
password = password(box_1)
print('Верный пароль:', password)