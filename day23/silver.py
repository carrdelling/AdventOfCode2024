from collections import defaultdict
from itertools import combinations


def get_triplets(graph):

    triples = set()

    for v in graph:
        neighbors = graph[v]

        for i, j in combinations(neighbors, 2):
            if j in graph[i]:
                t = tuple(sorted([v, i, j]))
                triples.add(t)

    return triples


def solve(data):

    edges = defaultdict(set)
    for row in data:
        a, b = row.strip().split('-')
        edges[a].add(b)
        edges[b].add(a)

    triplets = get_triplets(edges)

    with_t = 0
    for a, b, c in triplets:

        if any([a[0] == 't', b[0] == 't', c[0] == 't']):
            with_t += 1

    output = with_t

    return output


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = row.strip()
            input_.append(v)

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
