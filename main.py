def main():
    n_socks = input()
    socks = input().split(' ')

    socks = sorted(socks)
    pairs=0
    for each_sock in set(socks):
        pairs += int(socks.count(each_sock)/2)
    print(pairs)

main()