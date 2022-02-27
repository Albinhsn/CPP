def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print(from_rod,to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


n = int(input())
print(2**n - 1)
TowerOfHanoi(n, '1', '3', '2')