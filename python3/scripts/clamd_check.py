import sys

import clamd

if (len(sys.argv) < 2) or sys.argv[1] is None:
    raise ValueError("Please provide file name to scan.")

FILE_NAME = sys.argv[1]
CLAMD_SOCKET = {"ip_address": "clamav", "port": 3310}


def _client() -> type(clamd.ClamdNetworkSocket):
    return clamd.ClamdNetworkSocket(CLAMD_SOCKET["ip_address"], CLAMD_SOCKET["port"])


def _scan(file_name: str) -> type(clamd.ClamdNetworkSocket.instream):
    return _client().instream(open(file_name, "rb"))


def _infected(file_name: str) -> bool:
    result = _scan(file_name=file_name)
    if result.get("stream", [])[0] == "FOUND":
        return True

    return False


if __name__ == "__main__":
    _scan_result = _scan(file_name=FILE_NAME)
    _is_infected = str(_infected(file_name=FILE_NAME)).lower()
    print(
        f">> File '{FILE_NAME}' is infected: {_is_infected}. Virus found: {_scan_result['stream'][1]}."
    )
