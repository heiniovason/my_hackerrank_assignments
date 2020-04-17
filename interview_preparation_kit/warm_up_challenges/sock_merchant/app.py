def sockMerchant(n, ar):
    sock_pairs = None
    # constraint 1
    if n >= 1 and n <= 100:
        sock_pairs = 0
        sock_set = set()
        for sock in ar:
            i = ar.index(sock)
            # constraint 2
            if sock >= 1 and sock <= 100 and i >= 0 and i < n:
                if sock in sock_set:
                    sock_pairs += 1
                    sock_set.remove(sock)
                else:
                    sock_set.add(sock)
    return sock_pairs


if __name__ == '__main__':
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sockMerchant(n, ar))
