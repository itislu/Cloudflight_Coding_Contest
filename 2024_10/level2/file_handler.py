import os
import glob
from typing import Optional, Union, Callable, List, Tuple


class FileHandler:
    def __init__(
        self,
        directory: str = ".",
        delimiter: str = "\n",
        skip_lines: int = 0,
        in_suffix: str = ".in",
        out_suffix: str = ".out",
        file_numbers: Tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    ):
        self.directory: str = directory
        self.delimiter: str = delimiter
        self.skip_lines: int = skip_lines
        self.in_suffix: str = in_suffix
        self.out_suffix: str = out_suffix
        self.example_files: List[str] = glob.glob(
            f"{self.directory}/*_example{self.in_suffix}"
        )
        print(self.example_files)
        self.level: str = os.path.basename(self.example_files[0]).split("_")[0]
        digit_pattern = f"[{''.join(str(n) for n in file_numbers)}]"
        self.input_files: List[str] = glob.glob(
            f"{self.directory}/{self.level}_{digit_pattern}*{self.in_suffix}"
        )

    def process_all_files(
        self, algorithm: Callable[[str], str], test: bool = True
    ) -> None:
        if test and not self.test(algorithm):
            return
        print(f"{'All examples match! ' if test else ''} Processing all files...")
        for input_file in self.input_files:
            output_file = self._in_to_outfile(input_file)
            file = File(input_file, output_file, self.delimiter, self.skip_lines)
            file.process_file(algorithm)
            file.write_output()

    def test(self, algorithm: Callable[[str], str]) -> bool:
        for example_file in self.example_files:
            output_file = self._in_to_outfile(example_file)
            file = File(example_file, output_file, self.delimiter, self.skip_lines)
            output = file.process_file(algorithm)
            if not self._compare_with_example(file, output):
                return False
        return True

    def _compare_with_example(self, example: "File", output: str) -> bool:
        if not os.path.exists(example.output_file):
            print(f"{example.output_file} not found.")
            return False
        with open(example.output_file, "r") as f:
            example_output = f.read().strip()
        if output.strip() != example_output:
            print(
                f"Fail: Example output for {example.output_file} does not match.\n",
                f"Expected:\n{example_output}\n",
                f"Got:\n{output.strip()}",
            )
            return False
        print(f"Success: Example output for {example.output_file} matches!")
        return True

    def _in_to_outfile(self, filename: str) -> str:
        return filename.replace(self.in_suffix, self.out_suffix)


class File:
    def __init__(
        self,
        input_file: str,
        output_file: str,
        delimiter: str = "\n",
        skip_lines: int = 0,
    ):
        self.input_file: str = input_file
        self.output_file: str = output_file
        self.input_data: str
        self.output_data: str
        self.is_example: bool = "example" in self.input_file
        self.level: str = self.input_file.split("_")[0]
        self.delimiter: str = delimiter
        self.skip_lines: int = skip_lines

    def read_input(self) -> str:
        with open(self.input_file, "r") as f:
            lines = f.readlines()
        self.input_data = "".join(lines[self.skip_lines :]).strip()
        return self.input_data

    def write_output(
        self, output: Optional[Union[str, int]] = None, *, force: bool = False
    ) -> None:
        if output is None:
            output = self.output_data
        else:
            self.output_data = str(output)
        if not self.is_example or force:
            with open(self.output_file, "w") as f:
                f.write(self.output_data)
        else:
            print("Not writing example output.")

    def batch_generator(self):
        batches = self.input_data.split(self.delimiter)
        for batch in batches:
            yield batch.strip()

    def process_file(self, algorithm: Callable[[str], str]) -> str:
        self.read_input()
        processed_batches = [algorithm(batch) for batch in self.batch_generator()]
        self.output_data = self.delimiter.join(processed_batches)
        return self.output_data


def main() -> None:
    def algorithm(batch: str) -> str:
        return batch  # Placeholder

    handler = FileHandler()
    handler.process_all_files(algorithm)


if __name__ == "__main__":
    main()
