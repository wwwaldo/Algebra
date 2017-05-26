def decompose_cycles(bij):
    cycles = []
    dom = bij.keys()
    while dom:
        cycle = [dom.pop()]
        while bij[cycle[-1]] != cycle[0]:
            cycle.append(bij[cycle[-1]])
            dom.remove(cycle[-1])
        cycles.append(cycle)
    return cycles

def compose(bij1, bij2):
    bij = {}
    for k in bij2:
        bij[k] = bij1[bij2[k]]
    return bij

