from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_mode=True
        json_schema_extra={
            "example":{
            "username":"johndoe",
            "email":"johndoe@gmail.com",
             "password":"password",
             "is_staff":False,
             "is_active":False
             }
            }
        
class Settings(BaseModel):
    authjwt_secret_key:str='3fab0d60d9508371f7f8fc7b11c1ca304bef9ec9fab0679ae57c868502569a85'

class LogInModel(BaseModel):
    username:str
    password:str

class OrderModel(BaseModel):
    id:Optional[int]
    qty:int
    order_status:Optional[str]='PENDING'
    pizza_size:Optional[str]='SMALL'
    user_id:Optional[int]

    class Config:
        orm_mode=True
        json_schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }

class OrderStatusModel(BaseModel):
    order_status:Optional[str]='PENDING'

    class Config:
        orm_mode=True
        json_schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }
        


