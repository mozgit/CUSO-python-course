pi = 2.
delta = 1.
i = 0
while delta > 0.00000000001:
    i = i + 1
    delta = abs(pi - pi * (4. * i ** 2. / (4. * i ** 2. - 1.)))
    pi = pi * (4. * i ** 2. / (4. * i ** 2. - 1.))
print pi
