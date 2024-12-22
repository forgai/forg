from typing import AsyncGenerator, Dict, List, Optional, Tuple, Union

import requests
import websockets

from forgai.errors import BadRequest, NotFound, Unauthenticated


class Client:
    @classmethod
    def _get_http_headers(cls) -> Dict[str, str]:
        return {"Authorization": f"Bearer {forg.api_key}"}

    @classmethod
    def _get_ws_headers(cls) -> List[Tuple[str, str]]:
        return [("Authorization", f"Bearer {forg.api_key}")]

    @classmethod
    def _validate_response(cls, response: requests.Response) -> None:
        if response.status_code == 400:
            raise BadRequest(**response.json())
        if response.status_code == 401:
            raise Unauthenticated(**response.json())
        if response.status_code == 404:
            raise NotFound(**response.json())

    @classmethod
    def request_action(
        cls,
        method: str,
        action_path: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
    ) -> requests.Response:
        headers = cls._get_http_headers()
        url = f"https://{forg.api_base}/v1/{action_path}"
        r = requests.request(method, url, headers=headers, params=params, json=data)
        cls._validate_response(r)
        return r

    @classmethod
    def request_url(
        cls, method: str, url: str, data: Optional[Dict] = None
    ) -> requests.Response:
        headers = cls._get_http_headers()
        r = requests.request(method, url, headers=headers, json=data)
        cls._validate_response(r)
        return r

    @classmethod
    async def listen_to_execution(cls, address: str) -> Union[str, bytes]:
        headers = cls._get_ws_headers()
        url = f"wss://{forg.api_base}/ws/v1/execution/{address}/"
        async with websockets.connect(url, extra_headers=headers) as ws:
            return await ws.recv()
