states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])

stations: dict[str, set[str]] = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()




#if you want to cover all the states you should add this code into a while states_needed
print(stations.items())

while states_needed:  
    best_station = None
    states_covered: set[str] = set()
    for station, states_for_station in stations.items(): # go through (key, value) from dict
        covered = states_needed & states_for_station # intersect states needed and states for station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    if not states_covered:
        raise ValueError(f"Cannot cover all states. Uncovered: {states_needed}")

    states_needed -= states_covered
    final_stations.add(best_station)


if __name__ == "__main__":
    print(final_stations)