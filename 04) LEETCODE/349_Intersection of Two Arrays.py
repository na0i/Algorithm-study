class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))

        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        result = []

        if len_nums1 <= len_nums2:
            for i in range(len_nums1):
                target = nums1[i]

                # start_binary_search
                start = 0
                end = len_nums2 - 1

                while start <= end:
                    middle = (start + end) // 2
                    if nums2[middle] == target:
                        result.append(target)
                        break

                    elif nums2[middle] < target:
                        start = middle + 1

                    elif nums2[middle] > target:
                        end = middle - 1

        else:
            for i in range(len_nums2):
                target = nums2[i]

                # start_binary_search
                start = 0
                end = len_nums1 - 1

                while start <= end:
                    middle = (start + end) // 2
                    if nums1[middle] == target:
                        result.append(target)
                        break

                    elif nums1[middle] < target:
                        start = middle + 1

                    elif nums1[middle] > target:
                        end = middle - 1

        return result