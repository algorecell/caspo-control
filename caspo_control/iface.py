
def csv_of_minibn(bn):
    def str_of_lit(l):
        return "{}{}".format("!" if not l[1] else "", l[0])
    def str_of_clause(c):
        return "+".join(map(str_of_lit, c))
    rules = []
    for i, clauses in sorted(bn.as_dnf().items()):
        if isinstance(clauses, bool):
            raise TypeError("Boolean networks with constant nodes are not supported")
        for clause in clauses:
            rules.append("{}<-{}".format(i, str_of_clause(clause)))
    return "%s\n%s\n" % (",".join(rules), ",".join(["1"]*len(rules)))


