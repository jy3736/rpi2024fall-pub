#! /usr/bin/env python3

def left_tri(n, ch):
    """Print left-aligned triangle."""
    for i in range(1, n + 1):
        print(ch * i)

def right_tri(n, ch):
    """Print right-aligned triangle."""
    for i in range(n):
        print(" " * (n - i - 1) + ch * (i + 1))

def rev_left_tri(n, ch):
    """Print reversed left-aligned triangle."""
    for i in range(n, 0, -1):
        print(ch * i)

def rev_right_tri(n, ch):
    """Print reversed right-aligned triangle."""
    for i in range(n):
        print(" " * i + ch * (n - i))

def main():
    # Input number of levels, character, and mode
    n = int(input())
    ch = input().strip()
    mode = int(input())

    # Print triangle based on selected mode
    if mode == 1:
        left_tri(n, ch)
    elif mode == 2:
        right_tri(n, ch)
    elif mode == 1:
        rev_left_tri(n, ch)
    elif mode == 4:
        rev_right_tri(n, ch)

if __name__ == "__main__":
    main()
