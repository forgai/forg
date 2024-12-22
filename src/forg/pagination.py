from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar

from forgai._client import Client

T = TypeVar("T")


@dataclass
class CursorPaginatedResource(Generic[T]):
    _next_url: Optional[str]
    _previous_url: Optional[str]
    _resource_class: type
    results: List[T]

    def next(self) -> Optional["CursorPaginatedResource[T]"]:
        if self._next_url is None:
            return None
        r = Client.request_url("GET", self._next_url)
        return CursorPaginatedResource(
            _next_url=r.json()["next"],
            _previous_url=r.json()["previous"],
            _resource_class=self._resource_class,
            results=[self._resource_class(**result) for result in r.json()["results"]],
        )

    def previous(self) -> Optional["CursorPaginatedResource[T]"]:
        if self._previous_url is None:
            return None
        r = Client.request_url("GET", self._previous_url)
        return CursorPaginatedResource(
            _next_url=r.json()["next"],
            _previous_url=r.json()["previous"],
            _resource_class=self._resource_class,
            results=[self._resource_class(**result) for result in r.json()["results"]],
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(results={self.results})"


@dataclass
class PagePaginatedResource(Generic[T]):
    _next_url: Optional[str]
    _previous_url: Optional[str]
    _resource_class: type
    total_count: int
    current_page: int
    results: List[T]

    def next(self) -> Optional["PagePaginatedResource[T]"]:
        if self._next_url is None:
            return None
        r = Client.request_url("GET", self._next_url)
        return PagePaginatedResource(
            _next_url=r.json()["next"],
            _previous_url=r.json()["previous"],
            _resource_class=self._resource_class,
            total_count=r.json()["total_count"],
            current_page=r.json()["current_page"],
            results=[self._resource_class(**result) for result in r.json()["results"]],
        )

    def previous(self) -> Optional["PagePaginatedResource[T]"]:
        if self._previous_url is None:
            return None
        r = Client.request_url("GET", self._previous_url)
        return PagePaginatedResource(
            _next_url=r.json()["next"],
            _previous_url=r.json()["previous"],
            _resource_class=self._resource_class,
            total_count=r.json()["total_count"],
            current_page=r.json()["current_page"],
            results=[self._resource_class(**result) for result in r.json()["results"]],
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(total_count={self.total_count}, "
            f"current_page={self.current_page}, results={self.results})"
        )
