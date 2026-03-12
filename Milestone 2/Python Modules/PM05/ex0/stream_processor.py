from typing import Any, List, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    log_type: List[str] = ["ERROR", "INFO", "WARNING"]

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.count: int = 0
        self.total: int = 0
        self.average: float = 0

    def process(self, data: Any) -> str:
        for number in data:
            self.count += 1
            self.total += number
        self.average = self.total / self.count
        float_average: str = "%.1f" % self.average
        result: str = f"{self.count} {self.total} {float_average}"
        return result

    def validate(self, data: Any) -> bool:
        try:
            for number in data:
                number / 1
        except TypeError:
            return False
        return True

    def format_output(self, result: str) -> str:
        num: List[str] = result.split(" ")
        return f"Processed {num[0]} numeric values, sum={num[1]}, avg={num[2]}"


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.words: List[str] = []
        self.num_words: int = 0
        self.num_char: int = 0

    def process(self, data: Any) -> str:
        for word in self.words:
            self.num_words += 1
        for char in data:
            self.num_char += 1
        result: str = f"{self.num_char} {self.num_words}"
        return result

    def validate(self, data: Any) -> bool:
        try:
            self.words = data.split()
            if data.index(":"):
                return False
        except AttributeError:
            return False
        except ValueError:
            return True
        return True

    def format_output(self, result: str) -> str:
        num: List[str] = result.split(" ")
        return f"Processed text: {num[0]} characters, {num[1]} words"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.words: List[str] = []
        self.num_words: int = 0

    def process(self, data: Any) -> str:
        for word in self.words:
            self.num_words += 1
        if self.words[0] == "ERROR":
            result: str = f"[ALERT] ERROR level detected: {self.words[1]}"
        elif self.words[0] == "INFO":
            result: str = f"[INFO] INFO level detected: {self.words[1]}"
        else:
            result: str = f"[WARNING] WARNING level detected: {self.words[1]}"
        return result

    def validate(self, data: Any) -> bool:
        try:
            self.words = data.split(": ")
            for type in self.log_type:
                if self.words[0] == type:
                    return True
            return False
        except (AttributeError, IndexError):
            return False
        return True

    def format_output(self, result: str) -> str:
        return result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    result: str = ""
    num_arr: List[int] = [1, 2, 3, 4, 5]
    num_processor = NumericProcessor()
    print(f"\nInitializing Numeric Processor...\nProcessing data: {num_arr}")
    if num_processor.validate(num_arr):
        print("Validation: Numeric data verified\nOutput: ", end="")
        result = num_processor.process(num_arr)
        print(num_processor.format_output(result))

    text: str = "Hello Nexus World"
    string_processor = TextProcessor()
    print(f"\nInitializing Text Processor...\nProcessing data: \"{text}\"")
    if string_processor.validate(text):
        print("Validation: Text data verified\nOutput: ", end="")
        result = string_processor.process(text)
        print(string_processor.format_output(result))

    log: str = "ERROR: Connection timeout"
    log_processor = LogProcessor()
    print(f"\nInitializing Log Processor...\nProcessing data: \"{text}\"")
    if log_processor.validate(log):
        print("Validation: Log entry verified\nOutput: ", end="")
        result = log_processor.process(log)
        print(log_processor.format_output(result))

    print("\n=== Polymorphic Processing Demo ===\n")
    data_arr: List[Union[List[int], str]] = [
        [1, 2, 3],
        "Hi Evaluator",
        "INFO: System Ready"
    ]
    processors: List[Any] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    i: int = 1
    print("Processing multiple data types through same interface...")
    for processor in processors:
        for data in data_arr:
            if processor.validate(data):
                result = processor.process(data)
                print(f"Result {i}: {processor.format_output(result)}")
                i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
