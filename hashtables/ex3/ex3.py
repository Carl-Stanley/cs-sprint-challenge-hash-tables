def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cnt = {}

    for i in arrays:
        for n in i:
            if n not in cnt:
                cnt[n] = 0

            cnt[n] += 1

    result = [n for n, all in cnt.items() if all == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
