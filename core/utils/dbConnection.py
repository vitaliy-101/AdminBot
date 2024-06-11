import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def getAllRequests(self):
        query = "SELECT * FROM requests"
        return await self.connector.fetch(query)

