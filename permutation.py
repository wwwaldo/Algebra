class Permutation():
    def __init__(self, n, transform=dict()):
        """ initializer defaults to the identity if no transform dict is supplied"""
        assert isinstance(n, int), "n is not an int"
        self.n = n
        self.map = dict()
        input = list(range(n))
        if not transform:
            for el in input:
                self.map[el] = el
        else:
            assert len(transform) == n, "Invalid initializer!"
            self.map = transform

    def __len__(self):
        return self.n

    def __str__(self):
        """
        String representation of self in terms of disjoint cycles.
        No guarantees about ordering of the cycles because I'm dumb and set.pop() uses arbitrary order.
        :return:
        """
        cycle_repr = self.cycles()
        has_bracks = str(cycle_repr)
        cpy = has_bracks[1:-1]
        return cpy

    def cycles(self):
        """
        return a list of disjoint cycles representing self.
        Each disjoint cycle is also represented as a list.
        """
        cycles = list()

        input = list(range(self.n))
        remaining = set(range(self.n))
        while remaining:
            new_cycle = list()
            el = remaining.pop()
            new_cycle.append(el)
            next = self.apply(el)
            while next != el:
                new_cycle.append(next)
                remaining.remove(next)
                next = self.apply(next)
            cycles.append(new_cycle[:]) # !!! [:] is a slice op and forces a copy of the list.
            # Need to do it this way because I want to avoid naming conflicts.
        return cycles

    def apply(self, el):
        """
        Apply self to element el. Precondition: el < self.n.
        """
        assert isinstance(el, int), "el is not an int"
        assert el < self.n, "wrong dimension!"
        return self.map[el]

    def __eq__(self, other):
        if self.n != other.n:
            return False
        else:
            count = 0
            while count < self.n:
                if self.map[count] != other.map[count]:
                    return False
                count+= 1
            return True

    def __mul__(self, other):
        """ Group multiplication op (self compose other.)"""
        assert self.n == other.n, "Permutations have unequal dimension!"
        input = list(range(other.n))
        result = dict()
        for el in input:
            temp = other.apply(el)
            result[el] = self.apply(temp)
        permutation = Permutation(other.n, transform=result)
        return permutation

def generate_tables(permutations):
    """
    Print the time tables, given a list of permutations. Later I'll figure out some
    way of generating the canonical permutations efficiently.
    """
    # get the results
    ary, i, j = list(), 0, 0

    count = 0
    while count < len(permutations):
        ary.append(list())
        count2 = 0
        while count2 < len(permutations):
            ary[count].append("")
            count2+= 1
        count += 1

    for p1 in permutations: # row
        j = 0
        for p2 in permutations: # col
            ary[i][j] = p2 * p1
            j+= 1
        i+= 1

    k = 0
    while k < len(ary):
        curr = None
        nxt = max([len(str(p)) for p in ary[k]])
        if curr is None or nxt > curr:
            curr = nxt
        k +=1
    sepspace = curr
    print("*"*sepspace,end="")
    print(" | ",end="")

    # the initial row
    for p in permutations:
        spacing = " "*(sepspace - len(str(p)))
        print("{}{} | ".format(p, spacing), end="")
    print("")
    # dumb line separator printing
    print("-"*(3 + sepspace)*(len(permutations) + 1))

    i, j = 0, 0
        # print the table
    for p1 in permutations: # rows
        print(p1,end="")
        spacing = sepspace - len(str(p1))
        # print("spacing num is {}".format(spacing))
        print(spacing*" ", end="")
        print(" | ", end="")
        j = 0
        for p2 in permutations: # cols
            res = ary[i][j]
            print(res, end=""),
            print(" "*(sepspace - len(str(res))), end=""),
            print(" | ", end=""),
            j+= 1
        print("")
        i += 1
    return

if __name__ == '__main__':
    all = list()

    # make the identity
    t1 = dict()
    t1[0], t1[1], t1[2] = 0, 1, 2
    p1 = Permutation(3, t1)
    all.append(p1)

    # make (1)(2 3)
    t2 = dict()
    t2[0], t2[1], t2[2] = 0, 2, 1
    p2 = Permutation(3, t2)
    all.append(p2)

    # make (2)(1 3)
    t3 = dict()
    t3[0], t3[1], t3[2] = 2, 1, 0
    p3 = Permutation(3, t3)
    all.append(p3)

    # make (3)(1 2)
    t4 = dict()
    t4[0], t4[1], t4[2] = 1, 0, 2
    p4 = Permutation(3, t4)
    all.append(p4)

    # make the 1 - 2 - 3 shuffle
    t5 = dict()
    t5[0], t5[1], t5[2] = 1, 2, 0
    p5 = Permutation(3, t5)
    all.append(p5)

    #make (3 2 1)
    t6 = dict()
    t6[0], t6[1], t6[2] = 2, 0, 1
    p6 = Permutation(3, t6)
    all.append(p6)

    for el in all:
        print(el)

    generate_tables(all)