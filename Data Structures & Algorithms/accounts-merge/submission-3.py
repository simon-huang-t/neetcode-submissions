class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail_to_name = {}
        parent = {}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            root_a, root_b = find(a), find(b)
            parent[root_b] = root_a
        
        # 1) Initialization
        for name, *emails in accounts:
            for email in emails:
                mail_to_name[email] = name
                parent[email] = email
        # 2) Union
        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                union(first_email, email)
        # 3) Groups
        groups = defaultdict(list)
        for email in parent:
            # root = find(parent[email])
            root = find(email)
            groups[root].append(email)

        # 4)
        res = []
        for root, emails in groups.items():
            name = mail_to_name[root]
            res.append([name] + sorted(emails))
        return res