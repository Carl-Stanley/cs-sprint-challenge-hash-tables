def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    ws = {}
    for index, w in enumerate(weights):
        if w not in ws:
            ws[w] = index
    for item in range(length):

        item_weight = weights[item]
        nw = limit - item_weight
        if nw in ws and ws[nw] != item:
            return(max(item, ws[nw]), min(item, ws[nw]))
    return None
