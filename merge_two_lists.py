def get_overlap_ratio(a, b):
    a_left, a_right = a["positions"]
    b_left, b_right = b["positions"]
    
    overlap = max(0, min(a_right, b_right) - max(a_left, b_left))
    a_length = a_right - a_left
    b_length = b_right - b_left
    
    return overlap / a_length, overlap / b_length

def combine_element_lists(list1, list2):
    combined = list1 + list2
    combined.sort(key=lambda x: x["positions"][0])
    
    result = []
    used = [False] * len(combined)

    for i in range(len(combined)):
        if used[i]:
            continue

        current = combined[i]
        for j in range(i + 1, len(combined)):
            if used[j]:
                continue

            ratio1, ratio2 = get_overlap_ratio(current, combined[j])
            if ratio1 > 0.5 or ratio2 > 0.5:
                current["values"] += combined[j]["values"]
                used[j] = True

        result.append(current)
        used[i] = True

    return result
list1 = [
    {"positions": [0, 10], "values": [1]},
    {"positions": [15, 25], "values": [2]}
]

list2 = [
    {"positions": [8, 18], "values": [3]},
    {"positions": [30, 40], "values": [4]}
]

result = combine_element_lists(list1, list2)

for r in result:
    print(r)
