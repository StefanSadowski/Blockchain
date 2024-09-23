from hashlib import sha256
x = 5
y = 0  # We don't know what y should be yet...
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    print(y, sha256(f'{x*y}'.encode()).hexdigest())
    y += 1
print(y, sha256(f'{x*y}'.encode()).hexdigest())
print(f'The solution is y = {y}')