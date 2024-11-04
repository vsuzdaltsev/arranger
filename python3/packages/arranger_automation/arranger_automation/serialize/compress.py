"""Zip/unzip and encode/decode json serializable object."""

import base64
import json
from typing import Union
import zlib

from eusy_automation.sdlc import CustomTyping


def zip_json(
    json_structure: CustomTyping.JSONStructure,
    default: Union[type("function"), None] = None,
) -> str:
    """
    Convert json serializable object into zipped string encoded with base64.

    :param json_structure: Json object to compress.
    :param default: A function that gets called for objects that can’t otherwise be serialized.
    """
    try:
        return base64.b64encode(
            zlib.compress(json.dumps(json_structure, default=default).encode("UTF-8"))
        ).decode("ASCII")
    except BaseException as err:
        raise RuntimeError(
            ">> Could not zip data. Seems like it is not json serializable."
        ) from err


def unzip_json(json_string: str) -> CustomTyping.JSONStructure:
    """
    Decode and unzip json serializable object.

    :param json_string: Json object to uncompress.
    """
    try:
        return json.loads(zlib.decompress(base64.b64decode(json_string)))
    except BaseException as err:
        raise RuntimeError(">> Could not decode/unzip the contents.") from err
