"""Python typing extension."""

from typing import Any, AnyStr, Dict, List, Union


class CustomTyping:
    """Custom typing annotation types."""

    JSONObject = Dict[AnyStr, Any]
    JSONArray = List[JSONObject]
    JSONStructure = Union[JSONArray, JSONObject, str, None]
