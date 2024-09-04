#! /usr/bin/env python3

def main():
    rows = int(input())
    cols = int(input())

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print(f"{i * j:<6}", end="")
        print()

if __name__ == "__main__":
    main()
