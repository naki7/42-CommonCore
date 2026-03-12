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
    def __init__(self, id: str) -> None:
        super().__init__()
        self.id: str = id
        self.data_count: int = 0
        self.total: int = 0
        self.temp_count: int = 0
        self.average: float = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        for data in data_batch:
            self.data_count += 1
            if data.get("temp") is not None:
                self.total += data["temp"]
                self.temp_count += 1
        if self.temp_count > 0:
            self.average = self.total / self.temp_count
            float_average: str = "%.1f" % self.average
            filler_text: str = "readings processed, avg temp:"
            result: str = f"{self.data_count} {filler_text} {float_average}°C"
        else:
            result: str = ""
        return result

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        expect_input: List[str] = ["temp", "humidity", "pressure"]
        if isinstance(data_batch[0], str):
            return None
        first_key: List[str] = [key for key in data_batch[0]]
        key_found: bool = False
        for input in expect_input:
            if input == first_key[0]:
                key_found = True
                break
        if key_found is False:
            return None

        self.data_count = 0
        self.total = 0
        self.temp_count = 0
        self.average = 0

        if criteria is None:
            return data_batch
        filtered_data: List[Dict[str: int]] = []
        if criteria == "High-priority":
            for data in data_batch:
                if data.get("temp") and data["temp"] >= 40:
                    filtered_data.append({"temp": data["temp"]})
                elif data.get("humidity") and data["humidity"] >= 70:
                    filtered_data.append({"humidity": data["humidity"]})
                elif data.get("pressure") and data["pressure"] >= 1080:
                    filtered_data.append({"pressure": data["pressure"]})
            return filtered_data
        elif criteria == "Low-priority":
            for data in data_batch:
                if data.get("temp") and data["temp"] < 40:
                    filtered_data.append({"temp": data["temp"]})
                elif data.get("humidity") and data["humidity"] < 70:
                    filtered_data.append({"humidity": data["humidity"]})
                elif data.get("pressure") and data["pressure"] < 1080:
                    filtered_data.append({"pressure": data["pressure"]})
            return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str: int] = {"sensors": self.data_count}
        return stats


class TransactionStream(DataStream):
    def __init__(self, id: str) -> None:
        super().__init__()
        self.id: str = id
        self.count: int = 0
        self.net: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        for data in data_batch:
            self.count += 1
            if data.get("buy"):
                self.net += data["buy"]
            elif data.get("sell"):
                self.net -= data["sell"]
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
        first_key: List[str] = [key for key in data_batch[0]]
        key_found: bool = False
        for input in expect_input:
            if input == first_key[0]:
                key_found = True
                break
        if key_found is False:
            return None

        self.count = 0
        self.net = 0

        if criteria is None:
            return data_batch
        filtered_data: List[Dict[str: int]] = []
        if criteria == "High-priority":
            for data in data_batch:
                if (data.get("buy") and data["buy"] > 100):
                    filtered_data.append({"buy": data["buy"]})
                elif (data.get("sell") and data["sell"] > 100):
                    filtered_data.append({"sell": data["sell"]})
            return filtered_data
        elif criteria == "Low-priority":
            for data in data_batch:
                if (data.get("buy") and data["buy"] <= 100):
                    filtered_data.append({"buy": data["buy"]})
                elif (data.get("sell") and data["sell"] <= 100):
                    filtered_data.append({"sell": data["sell"]})
            return filtered_data
        else:
            filtered_data = [None]
            return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str: int] = {"trans": self.count}
        return stats


class EventStream(DataStream):
    def __init__(self, id: str) -> None:
        super().__init__()
        self.id: str = id
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

        self.count = 0
        self.errors = 0

        if criteria is None:
            return data_batch
        filtered_data: List[str] = []
        if criteria == "High-priority":
            for data in data_batch:
                if data == "error":
                    filtered_data.append("error")
            return filtered_data
        elif criteria == "Low-priority":
            for data in data_batch:
                if data == "login":
                    filtered_data.append("login")
                elif data == "logout":
                    filtered_data.append("logout")
            return filtered_data
        else:
            filtered_data = [None]
            return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str: int] = {"events": self.count}
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_streams(self, batches: List[Any]) -> None:
        if isinstance(batches[0], List) is False:
            batch_results: Dict[str: int] = {}
            for stream in self.streams:
                batch_results = stream.filter_data(batches, None)
                if batch_results is not None:
                    if isinstance(stream, SensorStream):
                        print("Sensor analysis: ", end="")
                    elif isinstance(stream, TransactionStream):
                        print("Transaction analysis: ", end="")
                    elif isinstance(stream, EventStream):
                        print("Event analysis: ", end="")
                    string_result: str = stream.process_batch(batch_results)
                    print(string_result)

        else:
            batch_results: Dict[str: int] = {
                "sensors": 0,
                "alerts": 0,
                "trans": 0,
                "large": 0,
                "events": 0,
                "errors": 0
            }
            print("Processing mixed stream types through unified interface...")
            for stream in self.streams:
                for batch in batches:
                    morphic_batch: List[Union[Dict[str: int], str]] = []
                    morphic_batch = stream.filter_data(batch, None)
                    if morphic_batch is not None:
                        stream.process_batch(morphic_batch)
                        batch_stats: Dict[str: int] = stream.get_stats()
                        if isinstance(stream, SensorStream):
                            batch_results["sensors"] += batch_stats["sensors"]
                        elif isinstance(stream, TransactionStream):
                            batch_results["trans"] += batch_stats["trans"]
                        elif isinstance(stream, EventStream):
                            batch_results["events"] += batch_stats["events"]

                    filtered_batch: List[Union[Dict[str: int], str]] = []
                    filtered_batch = stream.filter_data(batch, "High-priority")
                    if filtered_batch is not None:
                        stream.process_batch(filtered_batch)
                        batch_stats: Dict[str: int] = stream.get_stats()
                        if isinstance(stream, SensorStream):
                            batch_results["alerts"] += batch_stats["sensors"]
                        elif isinstance(stream, TransactionStream):
                            batch_results["large"] += batch_stats["trans"]
                        elif isinstance(stream, EventStream):
                            batch_results["errors"] += batch_stats["events"]

            print("\nBatch 1 Results:")
            print(f"- Sensor data: {batch_results['sensors']}",
                  "readings processed")
            print(f"- Transaction data: {batch_results['trans']}",
                  "operations processed")
            print(f"- Event data: {batch_results['events']}",
                  "events processed")

            print("\nStream filtering active: High-priority data only")
            print("Filtered results: ", end="")
            if batch_results["alerts"] > 0:
                print(f"{batch_results['alerts']} critical sensor alerts",
                      end="")
                if batch_results["large"] > 0 or batch_results["errors"] > 0:
                    print(", ", end="")
                else:
                    print("")
            if batch_results["large"] > 0:
                print(f"{batch_results['large']} large transaction", end="")
                if batch_results["errors"] > 0:
                    print(", ", end="")
                else:
                    print("")
            if batch_results["errors"] > 0:
                print(f"{batch_results['errors']} error events")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    initial_processor = StreamProcessor()
    initial_processor.add_stream(SensorStream("SENSOR_001"))
    initial_processor.add_stream(TransactionStream("TRANS_001"))
    initial_processor.add_stream(EventStream("EVENT_001"))

    print("\nInitializing Sensor Stream...")
    sensor_one: List[Dict[str: float]] = [{"temp": 22.5}, {"humidity": 65},
                                          {"pressure": 1013}]
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    print("Processing sensor batch: [", end="")
    for index in sensor_one:
        for key in index:
            print(f"{key}:{index[key]}", end="")
            if key != "pressure":
                print(", ", end="")
            else:
                print("]")
    initial_processor.process_streams(sensor_one)

    print("\nInitializing Transaction Stream...")
    trans_one: List[Dict[str: float]] = [{"buy": 100}, {"sell": 150},
                                         {"buy": 75}]
    print("Stream ID: TRANS_001, Type: Financial Data")
    print("Processing transaction batch: [", end="")
    for index in trans_one:
        for key in index:
            print(f"{key}:{index[key]}", end="")
            if index[key] != 75:
                print(", ", end="")
            else:
                print("]")
    initial_processor.process_streams(trans_one)

    print("\nInitializing Event Stream...")
    event_one: List[str] = ["login", "error", "logout"]
    print("Stream ID: EVENT_001, Type: System Events")
    print("Processing event batch: [", end="")
    for index in event_one:
        print(f"{index}", end="")
        if index != "logout":
            print(", ", end="")
        else:
            print("]")
    initial_processor.process_streams(event_one)

    print("\n=== Polymorphic Stream Processing ===")
    polymorphic_processor = StreamProcessor()
    polymorphic_processor.add_stream(SensorStream("SENSOR_002"))
    polymorphic_processor.add_stream(TransactionStream("TRANS_002"))
    polymorphic_processor.add_stream(EventStream("EVENT_002"))
    batch_one: List[List[Union[Dict[str: float], str]]] = [
        [{"temp": 43}, {"humidity": 70}],
        [{"buy": 100}, {"sell": 150}, {"buy": 75}, {"buy": 70}],
        ["login", "login", "logout"]
        ]
    polymorphic_processor.process_streams(batch_one)
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
