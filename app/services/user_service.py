class UserService:
    def __init__(self, repository):
        self.repository = repository
    
    async def create_user(self, user_data:UserBaseModel):
        user = await self.repository.create_user(user_data)
    
    async def read_user(self):
        return await self.repository.get_all_users()
    
    async def read_user_by_email(self, user_email: str):
        return await self.repository.get_user_by_email(user_email)
    
    async def update_user(self, user_data:UserBaseModel):
        return await self.repository.update_user(user_id, user_data)
    
    async def delete_user(self, user_id: int):
        return await self.repository.delete_user(user_id)