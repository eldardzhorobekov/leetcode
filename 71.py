class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for d in path.split('/'):
            if d == '..':
                if len(res):
                    res.pop()
            elif d not in ('', '.'):
                res.append(d)
        
        return '/' + '/'.join(res)
            
