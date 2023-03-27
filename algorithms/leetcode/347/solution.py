class Solution(object):
    def bucketSortSolution(self, nums, k):
        pass

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def bucketSortSolution(k):
            """
                case [1,1,1,2,2,3]:
                    countLookup = {1:3, 2:2, 3:1}
                              0   1   2   3   4   5   6
                    bucket = [    [3] [2] [1]    ]
                    res = [1, 2]
            """
            # Create empty lists whose index is their frequency
            bucket = [None]*(len(nums)+1)
            for i in range(len(bucket)):
                bucket[i] = []
            
            # Count the frequency of every number
            countLookup = collections.defaultdict(int)
            for n in nums:
                countLookup[n] += 1
            
            # Add elements to their frequency buckets
            for n in countLookup:
                bucket[countLookup[n]].append(n)
            
            # Reverse add frequency elements
            res = []
            i = len(bucket)-1
            while k > 0 and i >= 0:
                for b in bucket[i]:
                    res.append(b)
                    k -= 1
                    if k == 0:
                        break
                i -= 1
            return res
        
        def heapSolution(k):
            result = []
            mem = {}
            for i in range(len(nums)):
                if mem.get(nums[i], False):
                    mem[nums[i]] += 1
                else:
                    mem[nums[i]] = 1

            freq = []
            for key in mem:
                freq.append((mem[key], key))

            heap = freq[:k]
            heapq.heapify(heap)

            for i in range(k, len(freq)):
                if freq[i][0] > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, freq[i])

            result = []
            for x in heap:
                result.append(x[1])
            return result
        return heapSolution(k)
