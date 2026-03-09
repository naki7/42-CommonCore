from typing import Any, List, Union, Dict, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"processed": 0}


class SensorStream(DataStream):
    def __init__(self):
        super().__init__()
        self.data_count: int = 0
        self.total: int = 0
        self.temp_count: int = 0
        self.average: float = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        for data in data_batch:
            self.data_count += 1
            if data == "temp":
                self.total += data["temp"]
                self.temp_count += 1
        self.average = self.total / self.temp_count
        float_average: str = "%.1f" % self.average
        filler_text: str = "readings processed, avg temp:"
        result: str = f"{self.data_count} {filler_text} {float_average}°C"
        return result

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        expect_input: List[str] = ["temp", "humidity", "pressure"]
        if isinstance(data_batch[0], str):
            return None
        first_key: List[str] = data_batch[0].keys()
        key_found: bool = False
        for input in expect_input:
            if input == first_key[0]:
                key_found = True
                break
        if key_found is False:
            return None
        if Optional is None:
            return data_batch
        filtered_data: List[Dict[str: int]] = []
        if Optional == "High-priority":
            for data in data_batch:
                if data == "temp" and data_batch[data] >= 40:
                    filtered_data.append({data, data_batch[data]})
                elif data == "humidity" and data_batch[data] >= 70:
                    filtered_data.append({data, data_batch[data]})
                elif data == "pressure" and data_batch[data] >= 1080:
                    filtered_data.append({data, data_batch[data]})
            return filtered_data
        elif Optional == "Low-priority":
            for data in data_batch:
                if data == "temp" and data_batch[data] < 40:
                    filtered_data.append({data, data_batch[data]})
                elif data == "humidity" and data_batch[data] < 70:
                    filtered_data.append({data, data_batch[data]})
                elif data == "pressure" and data_batch[data] < 1080:
                    filtered_data.append({data, data_batch[data]})
            return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        plural: str = ""
        if self.count > 1:
            plural = "s"
        stats: Dict[str: int] = {
            f"critical sensor alert{plural}": self.data_count
            }
        return stats


class TransactionStream(DataStream):
    def __init__(self):
        super().__init__()
        self.count: int = 0
        self.net: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        for data in data_batch:
            self.count += 1
            if data == "buy":
                self.net += data_batch[data]
            elif data == "sell":
                self.net -= data_batch[data]
        filler_text: str = "operations, net flow:"
        net_sign: str = ""
        if self.net > 0:
            net_sign = "+"
        result: str = f"{self.count} {filler_text} {net_sign}{self.net} units"
        return result

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        expect_input: List[str] = ["buy", "sell"]
        if isinstance(data_batch[0], str):
            return None
        first_key: List[str] = data_batch[0].keys()
        key_found: bool = False
        for input in expect_input:
            if input == first_key[0]:
                key_found = True
                break
        if key_found is False:
            return None
        if Optional is None:
            return data_batch
        filtered_data: List[Dict[str: int]] = []
        if Optional == "High-priority":
            for data in data_batch:
                if data_batch[data] > 100:
                    filtered_data.append({data, data_batch[data]})
            return filtered_data
        elif Optional == "Low-priority":
            for data in data_batch:
                if data_batch[data] <= 100:
                    filtered_data.append({data, data_batch[data]})
            return filtered_data
        else:
            filtered_data = [None]
            return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        plural: str = ""
        if self.count > 1:
            plural = "s"
        stats: Dict[str: int] = {f"large transaction{plural}": self.count}
        return stats


class EventStream(DataStream):
    def __init__(self):
        super().__init__()
        self.count: int = 0
        self.errors: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        for data in data_batch:
            self.count += 1
            if data == "error":
                self.errors += 1
        filler_text: str = "events,"
        plural: str = "error detected"
        if self.errors > 1:
            plural = "errors detected"
        result: str = f"{self.count} {filler_text} {self.errors} {plural}"
        return result

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if isinstance(data_batch[0], Dict):
            return None
        if Optional is None:
            return data_batch
        filtered_data: List[str] = []
        if Optional == "High-priority":
            for data in data_batch:
                if data == "error":
                    filtered_data.append({data, data_batch[data]})
            return filtered_data
        elif Optional == "Low-priority":
            for data in data_batch:
                if data != "error":
                    filtered_data.append({data, data_batch[data]})
            return filtered_data
        else:
            filtered_data = [None]
            return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        plural: str = ""
        if self.count > 1:
            plural = "s"
        stats: Dict[str: int] = {f"error{plural} detected": self.errors}
        return stats


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(DataStream)

    def process_streams(self, streams: List[DataStream]) -> None:
        batch_results: Dict[str: int] = {}
        for stream in streams:
            for batch in stream:
                batch_results = stream.filter_data(batch)
                if batch_results is not None:
                    stream.process_batch(batch_results)
                    batch_results.append(stream.get_stats())
                    """change above to work with one stream at a time instead
                    of batching them"""
        filtered_batches: Dict[str: int] = {}
        for stream in streams:
            for batch in stream:
                filtered_batch: List[Union[Dict[str: int], str]] = []
                filtered_batch = stream.filter_data(batch, "High-priority")
                if filtered_batch[0] is not None:
                    stream.process_batch(filtered_batch)
                    filtered_batches.append(stream.get_stats())


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    """call streamprocessor"""


if __name__ == "__main__":
    main()
