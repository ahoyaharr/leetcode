from collections import deque

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def unpack(container):
            # if type(value) is list:
            #     # print('found list:', value)
            #     for element in value:
            #         unpack(element)
            # else:
            #     # print('found integer, adding {0} to queue'.format(value))
            #     self.queue.append(value)
            for element in container:
                if element.isInteger():
                    self.queue.append(element.getInteger())
                else:
                    unpack(element.getList())

        self.queue = deque()
        unpack(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0