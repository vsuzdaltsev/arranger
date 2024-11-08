"""Authenticate across AWS cloud resources using caller identity credentials."""


class DefaultCredentials:
    """AWS caller identity credentials."""

    @staticmethod
    def credentials():
        """Credentials dict."""
        return {
            "aws_access_key_id": None,
            "aws_secret_access_key": None,
            "aws_session_token": None,
        }
