import argparse
import re
import subprocess


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def measure_script(file_path: str) -> tuple[str, float]:
    output = subprocess.check_output(
        f"python -m cProfile -s cumtime {file_path}", shell=True
    )
    output = output.decode().strip()

    time_taken = re.search(r"in (?P<time>\d+\.\d+) seconds", output).group("time")
    result_output = output.splitlines()[0]

    return result_output, float(time_taken)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file1", required=True, type=str, help="Script 1 path")
    parser.add_argument("--file2", required=True, type=str, help="Script 2 path")

    args = parser.parse_args()

    script_1_result, script_1_time = measure_script(args.file1)
    script_2_result, script_2_time = measure_script(args.file2)
    assert (
        script_1_result == script_2_result
    ), f"Scripts are not equals : {script_1_result=}, {script_2_result=}"

    print(f"{script_1_result=}")
    print(f"{script_2_result=}")

    print(
        f"{bcolors.OKCYAN}{args.file2}{bcolors.ENDC} is {bcolors.OKGREEN} {script_1_time / script_2_time}x faster {bcolors.ENDC} than {bcolors.OKCYAN}{args.file1}{bcolors.ENDC}"
    )

    print(f"{bcolors.WARNING}{script_1_time=}s{bcolors.ENDC}")
    print(f"{bcolors.WARNING}{script_2_time=}s{bcolors.ENDC}")


if __name__ == "__main__":
    main()
