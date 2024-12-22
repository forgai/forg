from dataclasses import dataclass
from typing import Dict, List, Literal, Optional

from forgai._client import Client
from forgai.pagination import PagePaginatedResource
from forgai.resources._base import Resource


@dataclass
class Build(Resource):
    id: str
    agent_builder_job_id: str
    status: Literal["success", "in_progress", "failure"]
    logs: List[Dict[str, str]]
    created: str

    @classmethod
    def api_source(cls):
        return "builds"

    @classmethod
    def list(
        cls,
        agent_builder_job_id: Optional[str] = None,
        page: int = 1,
        page_size: int = 10,
    ) -> PagePaginatedResource["Build"]:
        params: Dict = {"page": page, "page_size": page_size}
        if agent_builder_job_id is not None:
            params["agent_builder_job_id"] = agent_builder_job_id
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
    def retrieve(cls, id: str) -> "Build":
        r = Client.request_action("GET", f"{cls.api_source()}/{id}/")
        return cls(**r.json())
