from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str | None = None
    # This is a field that will be used to check if the user is an admin
    # In this test project, we will allow user to create admin account
    is_admin: bool | None = False
