from typing import List, Union

from invoke import Context, Result

from arranger_automation.log import Log


def _validate_context(ctx: Context):
    if isinstance(ctx, Context):
        return ctx

    raise ValueError(f"Context must be instance of {type(Context)}.")


class DisposableEnvironment:
    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    def __init__(self, name: str, invoke_task_context: Union[Context, None] = None):
        self.log = Log().logger(desc=self.__class__.__name__)
        self.name = name
        self.context = _validate_context(ctx=invoke_task_context)

    def create(self) -> List[Result]:
        return self._run_commands(action_type="create")

    def delete(self) -> List[Result]:
        return self._run_commands(action_type="delete")

    def _run_commands(self, action_type=None):
        self.log.warning(f">> Run {action_type} commands: {self._create_commands()}")

        method_name = getattr(self, f"_{action_type}_commands")

        results = []
        for cmd in method_name():
            result = self.context.run(cmd)

            self.log.warning(f"{cmd} STDOUT: {result.stdout}.")
            self.log.warning(f"{cmd} STDERR: {result.stderr}.")
            self.log.warning(f"{cmd} EXITED: {result.exited}.")

            results.append(result)

        return results

    def _delete_commands(self) -> List:
        return [
            "inv -l",
        ]

    def _create_commands(self) -> List:
        return [
            "inv -l",
        ]
