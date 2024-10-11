numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1: #так как число 1 не является ни простым, ни составным числом, поэтому оно должно отсутствовать в конечных списках
        continue
    is_prime = True
    for j in range(2, i):
        if i % j ==0: #ищем кол-во делителей
            is_prime=False
            break

    if is_prime:
        primes.append(i) #составляем простых список чисел

    else:
        not_primes.append(i) #составляем непростых список чисел
print("Список простых числе: ", primes)
print("Список непростых числе: ", not_primes)