def hanoi(n, start, end, helper):
    """Move n >= 1 discs from start peg to end peg using helper peg."""
    if n == 1:
        print('Move top disc from ' + start + ' to ' + end)
    else:
        hanoi(n - 1, start, helper, end)    # Move all discs but the bottom one out of the way (the helper peg)
        hanoi(1, start, end, helper)        # Move 1 disc to the destination
        hanoi(n - 1, helper, end, start)    # Move the discs out of the way to the final destination

def main():
    n_discs = 64
    hanoi(n_discs, 'a', 'b', 'c')

if __name__ == '__main__': main()
