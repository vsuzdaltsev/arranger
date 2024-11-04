"""Manipulate with Slack thread."""

import json
import os
from typing import Dict, NoReturn

from slack_sdk import WebClient

from arranger_conf import AppConf
from arranger_automation.log import Log


GREEN = "#007C1A"
RED = "#FF0000"
ORANGE = "#FFC300"


class AzDeploymentsSlackTread:
    """Create, update Slack thread."""

    def __init__(self, channel_id: str = ""):
        self.log = Log().logger(desc=type(self).__name__)
        self.client = self._setup_slack_client()
        self.channel_id = channel_id
        self.parent_message_id = None

    def parent_message(self, initial_message: str):
        """Create first message in thread."""
        attachments = [
            {
                "fallback": "Upgrade your Slack client to use messages like these.",
                "color": ORANGE,
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": "STATUS: in progress"},
                    }
                ],
            }
        ]

        resp = self.client.chat_postMessage(
            channel=self.channel_id, text=initial_message, attachments=attachments
        )
        self.parent_message_id = resp.data["ts"]

        return resp.data["ts"]

    def additional_message(self, additional_message: str, color=None):
        """
        Add message to already created message.
        The first message becomes thread's parent message after this.
        """
        details = json.loads(additional_message)
        pipeline_name = details.get("pipeline_name")
        pipeline_id = details.get("pipeline_id")
        run_url = details.get("url")
        self.log.debug(f">> Run url: %s.", run_url)
        time_taken = details.get("time_taken")
        error = details.get("error")

        try:
            run_id = run_url.split("/")[-1]
            self.log.debug(f">> Run ID: %s.", run_id)
            result_url = "/".join(
                run_url.split("/")[0:-5] + ["_build"] + [f"results?buildId={run_id}"]
            )
            self.log.debug(f">> Result url: %s.", result_url)
        except ValueError as err:
            self.log.error(f">> Couldn't parse pipeline url: {run_url}. Error: {err}.")
            result_url = str(run_url) + error

        attachments = [
            {
                "fallback": "Upgrade your Slack client to use messages like these.",
                "color": self._colors()[color],
                "blocks": [
                    {"type": "section", "text": {"type": "mrkdwn", "text": result_url}}
                ],
            }
        ]

        return self.client.chat_postMessage(
            channel=self.channel_id,
            text=f"{pipeline_name}/{pipeline_id} ({round(time_taken)} seconds taken).",
            attachments=json.dumps(attachments),
            thread_ts=self.parent_message_id,
        )

    def update_message(
        self, update_message: str, color=None, custom_status="finished"
    ) -> NoReturn:
        """Update parent message."""
        attachments = [
            {
                "fallback": "Upgrade your Slack client to use messages like these.",
                "color": self._colors().get(color),
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": f"STATUS: {custom_status}"},
                    }
                ],
            }
        ]
        self.client.chat_update(
            channel=self.channel_id,
            ts=self.parent_message_id,
            text=update_message,
            attachments=attachments,
        )

    @staticmethod
    def _colors() -> Dict:
        return {"red": RED, "green": GREEN, None: ORANGE}

    def _setup_slack_client(self) -> type(WebClient):
        if not os.getenv("SLACK_BOT_TOKEN") or os.getenv("SLACK_BOT_TOKEN") == "":
            self.log.error(
                ">> Set 'SLACK_BOT_TOKEN' environment variable to be able to send messages."
            )
            raise RuntimeError("'SLACK_BOT_TOKEN' is not set.")

        return WebClient(token=os.getenv("SLACK_BOT_TOKEN"))


class AwsCodebuildSlackThread:
    """Create, update slack thread from within the AWS Codebuild."""

    def __init__(
        self,
        channel_id: str = AppConf.SLACK_CHANNELS.get("switchdev1", {})
        .get("test", {})
        .get("id"),
    ):
        self.log = Log().logger(desc=type(self).__name__)
        self.client = self._setup_slack_client()
        self.channel_id = channel_id
        self.parent_message_id = None

    def parent_message(self, initial_message: str):
        """Create first message in thread."""
        attachments = [
            {
                "fallback": "Upgrade your Slack client to use messages like these.",
                "color": ORANGE,
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": "STATUS: in progress"},
                    }
                ],
            }
        ]

        resp = self.client.chat_postMessage(
            channel=self.channel_id, text=initial_message, attachments=attachments
        )
        self.parent_message_id = resp.data["ts"]

        return resp.data["ts"]

    def additional_message(self, additional_message: str, color=None):
        """
        Add message to already created message.
        The first message becomes thread's parent message after this.
        """
        details = json.loads(additional_message)
        time_taken = details.get("time_taken")

        attachments = [
            {
                "fallback": "Upgrade your Slack client to use messages like these.",
                "color": self._colors()[color],
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": additional_message},
                    }
                ],
            }
        ]

        return self.client.chat_postMessage(
            channel=self.channel_id,
            text=f"({round(time_taken)} seconds taken).",
            attachments=json.dumps(attachments),
            thread_ts=self.parent_message_id,
        )

    def update_message(
        self, update_message: str, color=None, custom_status="finished"
    ) -> NoReturn:
        """Update parent message."""
        attachments = [
            {
                "fallback": "Upgrade your Slack client to use messages like these.",
                "color": self._colors().get(color),
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": f"STATUS: {custom_status}"},
                    }
                ],
            }
        ]
        self.client.chat_update(
            channel=self.channel_id,
            ts=self.parent_message_id,
            text=update_message,
            attachments=attachments,
        )

    @staticmethod
    def _colors() -> Dict:
        return {"red": RED, "green": GREEN, None: ORANGE}

    def _setup_slack_client(self) -> type(WebClient):
        if not os.getenv("SLACK_BOT_TOKEN") or os.getenv("SLACK_BOT_TOKEN") == "":
            self.log.error(
                ">> Set 'SLACK_BOT_TOKEN' environment variable to be able to send messages."
            )
            raise RuntimeError("'SLACK_BOT_TOKEN' is not set.")

        return WebClient(token=os.getenv("SLACK_BOT_TOKEN"))


class BulkBuildPipelineAwsCodebuildSlackThread(AwsCodebuildSlackThread):
    def additional_message(self, additional_message: str, color=None):
        """
        Add message to already created message.
        The first message becomes thread's parent message after this.
        """
        details = json.loads(additional_message)
        time_taken = details.get("time_taken")

        service = details.get("service")
        build_id = details.get("build_id")
        build_url = details.get("build_url")

        attachments = [
            {
                "fallback": "Upgrade your Slack client to use messages like these.",
                "color": self._colors()[color],
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"Service: {service}\nBuild URL: {build_url}\nBuild ID: {build_id}",
                        },
                    }
                ],
            }
        ]

        return self.client.chat_postMessage(
            channel=self.channel_id,
            text=f"({round(time_taken)} seconds taken).",
            attachments=attachments,
            thread_ts=self.parent_message_id,
        )
