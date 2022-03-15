class Solution:
    def simplifyPath(self, path):
        # Initialize a stack 
        res = []

        # Split the path by '/'
        splitPath = path.split('/')

        for i in range(len(splitPath)):
            # Pop to previous directory
            if splitPath[i] == '..' and res:
                res.pop()
            # Push valid path element
            elif splitPath[i] != '.' and splitPath[i] != '..' and splitPath[i] != '':
                res.append(splitPath[i])

        return '/' + '/'.join(res)
