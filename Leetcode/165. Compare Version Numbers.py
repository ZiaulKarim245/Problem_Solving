class Solution:
    def compareVersion(self, version1, version2):
        l1, l2 = [], []
        n = len(version1)
        left, right = 0, 0
        while right < n:
            if version1[left] == '0':
                left += 1
            if version1[right] == '.':
                if version1[left:right]:
                    l1.append(int(version1[left:right]))
                else:
                    l1.append(0)
                left = right + 1
            right += 1
        if version1[left:right]:
            l1.append(int(version1[left:right]))
        else:
            l1.append(0)

        n = len(version2)
        left, right = 0, 0
        while right < n:
            if version2[left] == '0':
                left += 1
            if version2[right] == '.':
                if version2[left:right]:
                    l2.append(int(version2[left:right]))
                else:
                    l2.append(0)
                left = right + 1
            right += 1
        if version2[left:right]:
            l2.append(int(version2[left:right]))
        else:
            l2.append(0)

        cnt1 = version1.count('.')
        cnt2 = version2.count('.')
        if cnt1 > cnt2:
            for i in range(cnt1 - cnt2):
                l2.append(0)
        elif cnt2 > cnt1:
            for i in range(cnt2 - cnt1):
                l1.append(0)

        if l1 > l2:
            return 1
        elif l2 > l1:
            return -1
        else:
            return 0



version1 = input()
version2 = input()
obj = Soluiton()
print(obj.compareVersion(version1, version2))