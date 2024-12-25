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


def make_lan(lan, edges):

    max_lan = {x for x in lan}

    increased = True
    while increased:
        increased = False

        for x in max_lan:

            for y in edges[x]:
                if edges[y].issuperset(max_lan):
                    max_lan.add(y)
                    increased = True
                    break

            if increased:
                break

    return max_lan


def solve(data):

    edges = defaultdict(set)
    for row in data:
        a, b = row.strip().split('-')
        edges[a].add(b)
        edges[b].add(a)

    triplets = get_triplets(edges)

    # grow the lan parties
    max_lan = set()
    for lan in triplets:

        new_lan = make_lan(lan, edges)

        if len(new_lan) > len(max_lan):
            max_lan = set(new_lan)

    output = ','.join(sorted(max_lan))

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
