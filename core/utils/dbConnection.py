import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def getAllPoints(self):
        query = "SELECT address FROM points"
        return await self.connector.fetch(query)

    # admin
    async def insertNewAdmin(self, data):
        pointName = "%" + data["admin_point"] + "%"
        idPoint = await self.connector.execute((f"SELECT id FROM points WHERE "
                                                f"address LIKE '{pointName}'"))
        idPoint = int(idPoint.split(" ")[-1])
        queryInsertIntoAdminsPoints = (f"INSERT INTO admins_points (id_admin, id_point) "
                                       f"VALUES({data['admin_id']}, {idPoint})")
        queryInsertNewAdmin = (f"INSERT INTO admins (id, first_name, last_name, "
                               f"phone, photo, passport) "
                               f"VALUES({data['admin_id']}, '{data['admin_first_name']}',"
                               f" '{data['admin_last_name']}', '{data['admin_phone']}', "
                               f" '{data['admin_photo_id']}', '{data['admin_passport']}')")
        await self.connector.execute(queryInsertNewAdmin)
        await self.connector.execute(queryInsertIntoAdminsPoints)

    async def getAdminAllData(self, id_admin):
        query = f"SELECT * FROM admins WHERE id = {id_admin}"
        return await self.connector.fetch(query)
