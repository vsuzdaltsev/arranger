"""
Run given function with a limited number of concurrent threads.
Common and AWS lambda adapted versions.
"""

from multiprocessing import cpu_count
from multiprocessing.dummy import Pool as ThreadPool
import os
from threading import Thread
from typing import Any, Callable, List

from arranger_automation.log import Log

MAX_THREADS = int(os.getenv("MAX_THREADS")) if os.getenv("MAX_THREADS") else cpu_count()
"""Maximum concurrent threads."""


class BasicParallel:
    """Run function decorated with 'each_slice' method."""

    @classmethod
    def each_slice(cls, func: Callable) -> Callable:
        """Decorator for throttling threads."""

        def go_threads(*args) -> None:
            if len(args) > 1:
                Log.logger(desc=cls.__name__).debug(
                    ">> Decorating instance method.. Object passed as a parameter."
                )
                obj = args[0]
                items_list = args[1]
            else:
                Log.logger(desc=cls.__name__).debug(
                    ">> Decorating function.. Object not passed as a parameter."
                )
                obj = None
                items_list = args[0]

            Log.logger(desc=cls.__name__).debug(">> Starting threads.")
            cls._process_concurrently(items_list=items_list, obj=obj, func=func)
            Log.logger(desc=cls.__name__).debug(">> Finishing threads.")

        return go_threads

    @staticmethod
    def add_obj(obj: Any, item: Any) -> List:
        """
        Pass object from decorated function to decorator.
        This is needed because a function may be decorated as well as a method.
        """
        return [obj, item] if obj else [item]

    @classmethod
    def _process_concurrently(
        cls, items_list: List, obj: Any, func: Callable
    ) -> None:
        Log.logger(desc=cls.__name__).error(
            ">> Subclass implementation needed. Parameters: %s, %s, %s.",
            items_list,
            obj,
            func,
        )


class Parallel(BasicParallel):
    """Run function decorated within environment which supports ThreadPool."""

    @classmethod
    def _process_concurrently(
        cls, items_list: List, obj: Any, func: Callable
    ) -> None:
        pool = ThreadPool(MAX_THREADS)
        pool.map(lambda x: func(*cls.add_obj(obj, x)), items_list)
        pool.close()
        pool.join()


class ParallelWithinLambda(BasicParallel):
    """Run function decorated within environment which doesn't support ThreadPool (like AWS lambda)."""

    @classmethod
    def _process_concurrently(
        cls, items_list: List, obj: Any, func: Callable
    ) -> None:
        threads = []
        while len(items_list) > 0:
            items_slice = [
                items_list.pop(0) for i, e in enumerate(items_list) if i < MAX_THREADS
            ]
            Log.logger(desc=cls.__name__).debug(
                ">> Processing concurrently: %s", items_slice
            )
            for item in items_slice:
                process = Thread(target=func, args=cls.add_obj(obj, item))
                process.start()
                threads.append(process)
            for process in threads:
                process.join()
