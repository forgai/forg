import asyncio
import json
from dataclasses import dataclass
from typing import Literal, Optional, Union

from forgai._client import Client
from forgai.pagination import PagePaginatedResource
from forgai.resources._base import Resource
from forgai.resources.agent_executor_job import AgentExecutorJob
from forgai.resources.execution import Execution
from forgai.types import JSON


@dataclass
class Agent(Resource):
    id: str
    name: str
    script: str
    requirements: str
    env_vars: str
    python_version: Literal["3.9", "3.10", "3.11", "3.12"]
    created: str
    modified: str

    @classmethod
    def api_source(cls):
        return "agents"

    @classmethod
    def list(cls, page: int = 1, page_size: int = 10) -> PagePaginatedResource["Agent"]:
        params = {"page": page, "page_size": page_size}
        r = Client.request_action("GET", f"{cls.api_source()}/", params=params)
        return PagePaginatedResource(
            _next_url=r.json()["next"],
            _previous_url=r.json()["previous"],
            _resource_class=cls,
            total_count=r.json()["total_count"],
            current_page=r.json()["current_page"],
            results=[cls(**result) for result in r.json()["results"]],
        )

    @classmethod
    def retrieve(cls, id: str) -> "Agent":
        r = Client.request_action("GET", f"{cls.api_source()}/{id}/")
        return cls(**r.json())

    @classmethod
    def create(
        cls,
        name: str,
        script: str,
        python_version: Literal["3.9", "3.10", "3.11", "3.12"],
        requirements: str = "",
        env_vars: str = "",
    ) -> "Agent":
        r = Client.request_action(
            "POST",
            f"{cls.api_source()}/create/",
            data={
                "name": name,
                "script": script,
                "requirements": requirements,
                "env_vars": env_vars,
                "python_version": python_version,
            },
        )
        return cls(**r.json())

    @classmethod
    def update(cls, id: str, **kwargs) -> "Agent":
        """
        The following fields can be updated: `name`, `script`, `requirements`,
        `env_vars`, `python_version`.
        """

        r = Client.request_action(
            "PATCH", f"{cls.api_source()}/{id}/update/", data=kwargs
        )
        return cls(**r.json())

    @classmethod
    def delete(cls, id: str) -> None:
        Client.request_action("DELETE", f"{cls.api_source()}/{id}/delete/")

    def execute(
        self, payload: JSON = None, wait: bool = True
    ) -> Union[Execution, AgentExecutorJob]:
        """
        Returns an `Execution` object if `wait` is `True`, otherwise returns a
        `AgentExecutorJob` object.
        """
        job = AgentExecutorJob.create(agent_id=self.id, payload=payload)

        if not wait:
            return job

        ret = asyncio.get_event_loop().run_until_complete(
            Client.listen_to_execution(job.execution_address)
        )
        return Execution(**json.loads(ret))
