def cfb():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f'{i}*{j}={i*j}  ', end="")
        print("\n", end="")


if __name__ == "__main__":
    cfb()
