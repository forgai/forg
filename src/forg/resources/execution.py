from dataclasses import dataclass
from typing import Dict, List, Literal, Optional

from forgai._client import Client
from forgai.pagination import CursorPaginatedResource
from forgai.resources._base import Resource
from forgai.types import JSON


@dataclass
class Execution(Resource):
    id: str
    agent_id: str
    agent_executor_job_id: Optional[str]
    status: Literal["success", "in_progress", "failure", "termination"]
    start: str
    finish: Optional[str]
    logs: List[Dict[str, str]]
    return_value: JSON

    @classmethod
    def api_source(cls) -> str:
        return "executions"

    @classmethod
    def list(
        cls,
        agent_id: Optional[str] = None,
        agent_executor_job_id: Optional[str] = None,
    ) -> CursorPaginatedResource["Execution"]:
        params = {}
        if agent_id is not None:
            params["agent_id"] = agent_id
        if agent_executor_job_id is not None:
            params["agent_executor_job_id"] = agent_executor_job_id
        r = Client.request_action("GET", f"{cls.api_source()}/", params=params)
        return CursorPaginatedResource(
            _next_url=r.json()["next"],
            _previous_url=r.json()["previous"],
            _resource_class=cls,
            results=[cls(**result) for result in r.json()["results"]],
        )

    @classmethod
    def retrieve(cls, id: str) -> "Execution":
        r = Client.request_action("GET", f"{cls.api_source()}/{id}/")
        return cls(**r.json())
