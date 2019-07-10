class NameSpace:

    def __init__(self, name, parent, args=None):
        if args is None:
            args = []
        self.name = name
        self.parent = parent
        self.args = args

    def __str__(self):
        if self.parent is not None:
            return '{ Name: ' + self.name + ', Parent: ' + self.parent.name + ', args: ' + str(self.args) + ' }'
        else:
            return '{ Name: ' + self.name + ', args: ' + str(self.args) + ' }'

    def add_arg(self, arg):
        self.args.append(arg)


def get_ns_by_name(name, d):
    for ns in d:
        if ns.name == name:
            return ns


def action(d):
    global result
    s = [i for i in input().split()]
    if s[0] == 'create':
        d.append(NameSpace(s[1], get_ns_by_name(s[2], d)))
    if s[0] == 'add':
        get_ns_by_name(s[1], d).add_arg(s[2])
    if s[0] == 'get':
        ns = get_ns_by_name(s[1], d)
        while ns is not None:
            if s[2] in ns.args:
                result += ns.name + '\n'
                return
            else:
                ns = ns.parent
        result += 'None' + '\n'
        return


a = int(input())
d = [NameSpace('global', None)]
result = ''
for i in range(a):
    action(d)
print(result)
