from typing import Any, TypedDict


class ProcessorReplaceConfig(TypedDict):
    column_name: str
    values: dict[Any, Any]
