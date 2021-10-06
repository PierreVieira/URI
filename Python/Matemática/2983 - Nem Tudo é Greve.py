def primo(x):
    if x <= 1:
        return False
    for c in range(2, int(x ** 0.5) + 1):
        if x % c == 0 and c != x:
            return False
    return True


primos = sorted(list(filter(primo, list(set([int(input()) for _ in range(int(input()))])))))
quantidade_primos = len(primos)
print(quantidade_primos)
if quantidade_primos > 0:
    print(f"{str(primos)[1:-1]}.")
else:
    print('')
