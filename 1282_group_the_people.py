from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = list()
        group_dictionary = dict()

        for id in range(len(groupSizes)):
            group_size = groupSizes[id]
            if group_size not in group_dictionary or len(group_dictionary[group_size]) == group_size:
                group = [id]
                groups.append(group)
                group_dictionary[group_size] = group
            else:
                group_dictionary[group_size].append(id)

        return groups