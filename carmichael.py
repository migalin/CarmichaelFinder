import itertools

# prime numbers' limits
limits = 3, 110
# how many divisors should Carmichael number have
divisors = 8

# find primes in limits
primes = []
for el in range(*limits):
    is_prime = True
    for num in range(2, int(el ** 0.5) + 1):
        if el % num == 0:
            is_prime = False
            break
      
    if is_prime:
        primes.append(el)

print("We try to use these prime numbers: ", primes)
print("Process started...")

for el in itertools.combinations(primes, divisors):
	carm = True
	m = 1
	for divisor in el:
		m *= divisor
	m_minus_one = m - 1
	for divisor in el:
		if m_minus_one % (divisor - 1):
			carm = False
			break
	if carm:
		print("Carmichael number", m, '=', "*".join(map(str,el)),"was found")
