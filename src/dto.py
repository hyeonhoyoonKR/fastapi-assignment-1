from pydantic import BaseModel, field_validator, ConfigDict
import re

class CreateUserRequest(BaseModel):
    name: str
    phone_number: str
    height: float
    bio: str | None = None

    model_config = ConfigDict(strict=True)

    @field_validator('phone_number')
    def check_phone_number(cls, phone_number: str):
        pn = r'010-\d{4}-\d{4}'
        if not re.match(pn, phone_number):
            raise ValueError('올바른 전화번호 형식으로 입력해주세요. (010-XXXX-XXXX)')
        return phone_number

    @field_validator('bio')
    def check_bio(cls, bio: str | None):
        if bio != None:
            if len(bio) > 500:
                raise ValueError('bio 필드의 길이는 500자를 초과할 수 없습니다.')
        return bio

class UserResponse(BaseModel):
    user_id: int
    name: str
    phone_number: str
    height: float
    bio: str | None