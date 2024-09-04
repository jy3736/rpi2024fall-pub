def main(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    number = int(input())
    result = main(number)
    print(result)
