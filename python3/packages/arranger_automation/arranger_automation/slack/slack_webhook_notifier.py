"""Slack notifications."""

import json
from typing import Dict

import requests

from arranger_conf import AppConf
from arranger_automation.log import Log


GREEN = "#007C1A"
RED = "#007C1A"


class SlackNotifier:
    """Send properly formatted notification message to the proper slack channel."""

    HEADERS = {"Content-type": "application/json"}

    def __init__(self, message: str, notification_endpoint: str = ""):
        self.log = Log().logger(desc=type(self).__name__)
        self.message = message
        self.notification_endpoint = notification_endpoint

    def send_message(self) -> int:
        """Send message to given notification endpoint linked with proper slack channel."""
        payload = json.dumps(self._formatter())
        response = requests.post(
            self.notification_endpoint, headers=self.HEADERS, data=payload
        )
        self.log.debug(">> Response: %s", response.__dict__)

        return response.status_code

    def _formatter(self) -> Dict:
        return {"text": self.message}

    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"


class DeploySlackNotifier(SlackNotifier):
    """Notifier for deployment pipelines."""

    def _formatter(self) -> Dict:
        message = json.loads(self.message)
        pipeline_id = message.get("pipeline_id")
        pipeline_name = message.get("pipeline_name")
        pipeline_run_url = message.get("url")
        pipeline_result = message.get("result")

        def pipeline_run_web_url(run_url: str) -> str:
            try:
                run_id = run_url.split("/")[-1]
                result = "/".join(
                    run_url.split("/")[0:-5]
                    + ["_build"]
                    + [f"results?buildId={run_id}"]
                )
            except BaseException as err:
                raise RuntimeError(
                    f">> Can't get proper pipeline run url. Error: {err}"
                ) from err
            return result

        def color(get_from: Dict = message) -> str:
            if get_from.get("result") == "succeeded":
                return GREEN
            return RED

        self.log.debug(
            f">> Pipeline run web url: {pipeline_run_web_url(pipeline_run_url)}"
        )
        self.log.debug(f">> Pipeline result: {pipeline_result}")

        return {
            "text": f"Pipeline {pipeline_id}/{pipeline_name} has completed.",
            "attachments": [
                {
                    "color": color(get_from=message),
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"STATUS: {pipeline_result}\nURL: {pipeline_run_web_url(pipeline_run_url)}",
                            },
                        }
                    ],
                }
            ],
        }
