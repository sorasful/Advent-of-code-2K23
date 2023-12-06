from collections import defaultdict

text = """Time:        60     94     78     82
Distance:   475   2138   1015   1650"""


time_line, distance_line = text.split("\n")

races = defaultdict(dict)

for i, (time, distance) in enumerate(zip(time_line.split(), distance_line.split())):
    # skip the first one since it's only the texts
    if i == 0:
        continue

    races[i]["time"] = int(time)
    races[i]["distance"] = int(distance)


def calculate_ways_to_beat_race(time: int, distance_to_beat: int) -> list[int]:
    """
    Returns the time to hold the boat to win the race.
    """
    # go backwards
    valid_times = []
    for time_to_hold in range(time, 0, -1):
        remaining_time = time - time_to_hold
        time_to_race = time - remaining_time
        distance_ran = time_to_race * remaining_time

        if distance_ran > distance_to_beat:
            valid_times.append(time_to_hold)

    return valid_times


tot_results = 1
for race_nb, race in races.items():
    results = calculate_ways_to_beat_race(
        time=race["time"], distance_to_beat=race["distance"]
    )
    tot_results *= len(results)
print(tot_results)
