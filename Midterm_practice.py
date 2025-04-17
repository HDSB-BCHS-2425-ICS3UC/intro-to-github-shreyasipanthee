for i in range (0,101):
    for k in range(1, int(i**0.5) + 1):
        if i % k == 0:
            print(f"{ k } is a factor of { i }")
            if k != i // k:  # Avoid duplicate factors
                print(f"{i // k} is a factor of {i}")