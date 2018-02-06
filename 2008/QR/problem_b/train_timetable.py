from collections import namedtuple

TripData = namedtuple('TripData', ['departure', 'arrival', 'start_st'])


def insert_ordered(seq, value):
    """Insert value into ordered sequence, without violating the order."""
    for idx, elem in enumerate(seq):
        if elem > value:
            seq.insert(idx, value)
            return
    seq.append(value)

def count_needed_trains(trips, turnaround):
    """Count trains needed to serve given trips assuming given turnaround."""
    available = [[], []]
    trips = sorted(trips)
    counts = [0, 0]
    for trip in trips:
        if available[trip.start_st] and available[trip.start_st][0] <= trip.departure:
            available[trip.start_st].pop(0)
        else:
            counts[trip.start_st] += 1
        insert_ordered(available[1-trip.start_st], trip.arrival + turnaround)
    return counts

def hhmm_to_number(hhmm):
    """Convert string of the form HH:MM to number representing minutes from midnight."""
    parts = hhmm.split(':')
    return int(parts[0]) * 60 + int(parts[1])

def read_trip(station):
    """Read a single trip from stdin."""
    times = input().split()
    return TripData(hhmm_to_number(times[0]), hhmm_to_number(times[1]), station)

def read_case():
    """Read whole test case from stdin."""
    turnaround = int(input())
    n_ab, n_ba = (int(x) for x in input().split())
    return [read_trip(0) for _ in range(n_ab)] + [read_trip(1) for _ in range(n_ba)], turnaround

def main():
    """Entrypoint of this script."""
    n_cases = int(input())
    for i in range(n_cases):
        print('Case #{0}: {1} {2}'.format(i+1, *count_needed_trains(*read_case())))

if __name__ == '__main__':
    main()
