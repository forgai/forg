from dataclasses import dataclass
from typing import Optional

from forgai._client import Client
from forgai.pagination import CursorPaginatedResource
from forgai.resources._base import Resource
from forgai.types import JSON


@dataclass
class AgentExecutorJob(Resource):
    id: str
    agent_id: str
    execution_address: str
    created: str

    @classmethod
    def api_source(cls):
        return "agent-executor-jobs"

    @classmethod
    def list(
        cls,
        agent_id: Optional[str] = None,
    ) -> CursorPaginatedResource["AgentExecutorJob"]:
        params = {}
        if agent_id is not None:
            params["agent_id"] = agent_id
        r = Client.request_action("GET", f"{cls.api_source()}/", params=params)
        return CursorPaginatedResource(
            _next_url=r.json()["next"],
            _previous_url=r.json()["previous"],
            _resource_class=cls,
            results=[cls(**result) for result in r.json()["results"]],
        )

    @classmethod
    def retrieve(cls, id: str) -> "AgentExecutorJob":
        r = Client.request_action("GET", f"{cls.api_source()}/{id}/")
        return cls(**r.json())

    @classmethod
    def create(cls, agent_id: str, payload: JSON = None) -> "AgentExecutorJob":
        r = Client.request_action(
            "POST",
            f"{cls.api_source()}/create/",
            data={"agent_id": agent_id, "payload": payload},
        )
        return cls(**r.json())
