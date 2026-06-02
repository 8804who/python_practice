class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        gas_amount = 0
        start = 0
        for i in range(len(gas)):
            gas_amount += gas[i]
            gas_amount -= cost[i]

            if gas_amount < 0:
                gas_amount = 0
                start = i+1
        return start