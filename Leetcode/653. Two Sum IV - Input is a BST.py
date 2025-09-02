class Solution:
    def findTarget(self, root, k) -> bool:
        # values = []
        # def bfs(node):
        #     if not node:
        #         return 
        #     values.append(node.val)
        #     bfs(node.left)
        #     bfs(node.right)

        # bfs(root)

        # values.sort()
        # left, right = 0, len(values) - 1
        # while left < right:
        #     if values[left] + values[right] == k:
        #         return True
        #     elif values[left] + values[right] > k:
        #         right -= 1
        #     else:
        #         left += 1
        # return False

        store = set()
        def bfs(node):
            if not node:
                return False
            if (k - node.val) in store:
                return True
            store.add(node.val)
            return bfs(node.left) or bfs(node.right)
        return bfs(root)

root = input()
k = int(input())
obj = Solution()
print(obj.findTarget(root, k))