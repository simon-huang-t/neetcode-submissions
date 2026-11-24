class DSU:
    def __init__(self):
        self.parents = defaultdict(str)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        self.parents[root_b] = root_a

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        mail_to_account = defaultdict(str)
        dsu = DSU()
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                dsu.parents[email] = email
                mail_to_account[email] = name
        for account in accounts:
            for i in range(2, len(account)):
                dsu.union(dsu.parents[account[1]], dsu.parents[account[i]])
        groups = defaultdict(list)
        for email in dsu.parents:
            root = dsu.find(email)
            groups[root].append(email)
        for main_email, emails in groups.items():
            name = mail_to_account[main_email]
            res.append([name] + sorted(emails))
        return res