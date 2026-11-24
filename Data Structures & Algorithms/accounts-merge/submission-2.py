class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = {} #mail --> root_mail
        mail_to_name = {}

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(a, b):
            root_a, root_b = find(a), find(b)
            parents[root_b] = root_a

        # 1) Init
        for name, *emails in accounts:
            for email in emails:
                mail_to_name[email] = name
                parents[email] = email

        # 2) Union
        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                union(first_email, email)

        #3) Group by emails
        groups = defaultdict(list) # root_mail --> [emails]
        for email in parents:
            root = find(email)
            groups[root].append(email)

        #4) Create result
        res = []
        for email, emails in groups.items():
            name = mail_to_name[email]
            res.append([name] + sorted(emails))
        return res
