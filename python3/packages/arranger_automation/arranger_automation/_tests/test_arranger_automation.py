import pytest

from arranger_automation.validate import InvalidSubnet, ValidateSubnets


VALID_RANGES = {
    "vnet1": {
        "cidr": ["10.41.0.0/18"],
        "description": None,
        "legacy_name": None,
        "subnets": {
            "snet-1": {
                "cidr": ["10.41.0.0/20"],
                "description": None,
                "legacy_name": None,
            },
            "snet-2": {
                "cidr": ["10.41.16.0/20"],
                "description": None,
                "legacy_name": None,
            },
        },
    }
}

INVALID_RANGES = {
    "vnet1": {
        "cidr": ["10.41.0.0/18"],
        "description": None,
        "legacy_name": None,
        "subnets": {
            "this-snet-is-not-a-subnet-for-vnet-cidr": {
                "cidr": ["10.88.0.0/20"],
                "description": None,
                "legacy_name": None,
            },
        },
    }
}


class TestValidateSubnets:
    @staticmethod
    def test_validate_with_valid_ranges():
        assert ValidateSubnets(ranges=VALID_RANGES).validate() == VALID_RANGES

    @staticmethod
    @pytest.mark.xfail(raises=InvalidSubnet)
    def test_validate_with_invalid_ranges():
        with pytest.raises(InvalidSubnet):
            ValidateSubnets(ranges=INVALID_RANGES).validate()
