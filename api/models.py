import typing as t

import aiohttp


class HttpClient:
    """HTTP client used for requests."""

    _session: t.Optional[aiohttp.ClientSession] = None
    _tcp_session: t.Optional[aiohttp.ClientSession] = None

    def start(self) -> None:
        """Start the client."""
        self._session = aiohttp.ClientSession()
        self._tcp_session = aiohttp.ClientSession(connector=aiohttp.TCPConnector())

    @property
    def session(self) -> aiohttp.ClientSession:
        """Return the session, raising an error if there isn't any."""
        if not self._session:
            raise ValueError("Instance isn't started")
        return self._session

    @property
    def tcp_session(self) -> aiohttp.ClientSession:
        """Return the tcp session, raising an error if there isn't any."""
        if not self._tcp_session:
            raise ValueError("Instance isn't started")
        return self._tcp_session

    async def stop(self) -> None:
        """Stop the client"""
        await self.session.close()
        await self.tcp_session.close()

        self._session = None
        self._tcp_session = None

    def __call__(self) -> aiohttp.ClientSession:
        return self.session
