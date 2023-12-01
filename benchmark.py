import argparse
import subprocess


def execute_script(file_path: str) -> str:
    output = subprocess.check_output(f"python {file_path}", shell=True)

    return output.decode().strip()


def measure_script(file_path: str) -> str:
    output = subprocess.check_output(
        f"python -m cProfile -s cumtime {file_path} | grep 'function calls'", shell=True
    )
    output = output.decode().strip()

    print(f"{output} -> {file_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file1", required=True, type=str, help="Script 1 path")
    parser.add_argument("--file2", required=True, type=str, help="Script 2 path")

    args = parser.parse_args()

    output1 = execute_script(args.file1)
    output2 = execute_script(args.file2)

    assert output1 == output2, f"Scripts are not equals : {output1=}, {output2=}"

    measure_script(args.file1)
    measure_script(args.file2)


if __name__ == "__main__":
    main()
