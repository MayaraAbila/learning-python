def maior(*nums):  # desempacotamento
    m = 0
    for v in nums:
        if v > m:
            m = v
    print('--'*20)
    print(
        f'Foram informados {len(nums)} números ao todo e o maior valor foi o {m}.')
    print('--'*20)


maior(12, 4, 67, 90, 50)
maior(23, 45, 2, 8, 10, 34, 13, 21, 34, 56)
