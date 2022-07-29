from __future__ import annotations

from aiohttp import ClientSession, TCPConnector


class HTTPClient:
    _session: ClientSession | None = None
    _tcp_session: ClientSession | None = None

    def __init__(self) -> None:
        self._session = ClientSession()
        self._tcp_session = ClientSession(connector=TCPConnector())

    @property
    def session(self) -> ClientSession:
        if not self._session:
            raise ValueError("AIOHTTP session not initialized.")

        return self._session

    @property
    def tcp_session(self) -> ClientSession:
        if not self._tcp_session:
            raise ValueError("TCP session not initialized.")

        return self._tcp_session

    async def stop(self) -> None:
        """Stop the client"""
        await self.session.close()
        await self.tcp_session.close()

        self._session = None
        self._tcp_session = None

    def __call__(self) -> ClientSession:
        return self.session
