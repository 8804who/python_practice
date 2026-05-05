from collections import deque

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []

        q = deque()
        q.append((s[0], 0))

        while q:
            string, idx = q.popleft()
            valid = True
            nums = string.split(".")
            for num in nums:
                if (num[0] == '0' and len(num) >= 2) or int(num) > 255:
                    valid = False
                    break
            if not valid:
                continue
            if idx == len(s)-1:
                if string.count('.') == 3:
                    answer.append(string)
                continue
            idx += 1
            q.append((string+s[idx], idx))
            if string.count('.') < 4:
                q.append((string+'.'+s[idx], idx))

        return answer