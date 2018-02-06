"""Solution to Problem A in GCJ 2008 Qualification Round."""

def count_switches(engines, queries):
    """Count switches in given query list."""
    switches = 0
    seen = set()
    for query in queries:
        if query not in seen and len(seen) == len(engines) - 1:
            switches += 1
            seen.clear()
        seen.add(query)
    return switches

def read_case():
    """Read case from stdin."""
    n_engines = int(input())
    engines = [input() for _ in range(n_engines)]
    n_queries = int(input())
    queries = [input() for _ in range(n_queries)]
    return engines, queries


def main():
    """Entrypoint of this script."""
    n_cases = int(input())
    for i in range(n_cases):
        print('Case #{0}: {1}'.format(i+1, count_switches(*read_case())))

if __name__ == '__main__':
    main()
