def jumpingOnClouds(c):
    skips = 0
    counter = 0
    if len(c) >= 2 and len(c) <= 100:
        for cl in c:
            if cl == 0:
                counter += 1
                if counter == 3:
                    skips += 1
                    counter = 1
            elif cl == 1:
                skips += 1
                counter = 0
            else:
                msg = '"{}" is not a valid type of cloud.'.format(cl)
                raise ValueError(msg)
    else:
        msg = '"{}" is not a valid cloud range.'.format(len(c))
        raise ValueError(msg)
    return len(c) - 1 - skips


if __name__ == '__main__':

    # Expected = 3 jumps
    c1 = [0, 0, 0, 0, 1, 0]
    print('Total jumps c1 = {0}'.format(
        jumpingOnClouds(c1)
        ))

    # Expected = 4 jumps
    c2 = [0, 0, 1, 0, 0, 1, 0]
    print('Total jumps c2 = {0}'.format(
        jumpingOnClouds(c2)
        ))

    # Expected = not a valid type of cloud
    # c3 = [0, 0, 2, 1, 0, 0]
    # print('Total jumps c3 = {0}'.format(
    #    jumpingOnClouds(c3)
    #    ))

    # Expected = not a valid cloud range
    # c4 = [0]
    # print('Total jumps c4 = {0}'.format(
    #    jumpingOnClouds(c4)
    #    ))

    # Expected = 6 jumps
    c5 = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    print('Total jumps c5 = {0}'.format(
        jumpingOnClouds(c5)
        ))

    # Expected = 28 jumps
    c6 = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
          0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1,
          0, 1, 0, 0]
    print('Total jumps c6 = {0}'.format(
        jumpingOnClouds(c6)
        ))

    # Expected = 54 jumps
    c7 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
          0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0,
          1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0,
          1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1,
          0, 1, 0, 0, 0, 0, 1, 0]
    print('Total jumps c7 = {0}'.format(
        jumpingOnClouds(c7)
        ))
