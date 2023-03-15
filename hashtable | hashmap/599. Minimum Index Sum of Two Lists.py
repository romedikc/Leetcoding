from typing import List


def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
    index_sum = {}
    for i, v in enumerate(list1):
        if v in list2:
            index_sum[v] = i + list2.index(v)

    min_sum = min(index_sum.values())
    return [k for k, v in index_sum.items() if v == min_sum]


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(findRestaurant(list1, list2))
