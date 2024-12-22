from dataclasses import dataclass
from typing import Dict, Optional

from forgai._client import Client
from forgai.pagination import PagePaginatedResource
from forgai.resources._base import Resource


@dataclass
class AgentBuilderJob(Resource):
    id: str
    agent_id: str
    created: str

    @classmethod
    def api_source(cls):
        return "agent-builder-jobs"

    @classmethod
    def list(
        cls, agent_id: Optional[str] = None, page: int = 1, page_size: int = 10
    ) -> PagePaginatedResource["AgentBuilderJob"]:
        params: Dict = {"page": page, "page_size": page_size}
        if agent_id is not None:
            params["agent_id"] = agent_id
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
    def retrieve(cls, id: str) -> "AgentBuilderJob":
        r = Client.request_action("GET", f"{cls.api_source()}/{id}/")
        return cls(**r.json())
