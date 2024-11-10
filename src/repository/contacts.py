from typing import List

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas.contacts import ContactRequest
from datetime import datetime


# async def get_tags(skip: int, limit: int, db: Session) -> List[Tag]:
#     return db.query(Tag).offset(skip).limit(limit).all()
#
#
# async def get_tag(tag_id: int, db: Session) -> Tag:
#     return db.query(Tag).filter(Tag.id == tag_id).first()



async def create_contact(body: ContactRequest, db: Session) -> Contact:
    if body.birthday == '':
        contact = Contact(name=body.name, last_name=body.last_name, email=body.email, phone=body.phone, info=body.info)
    else:
        contact = Contact(name=body.name, last_name=body.last_name, email=body.email, phone=body.phone, info=body.info,
                          birthday=body.birthday)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


# async def update_tag(tag_id: int, body: TagModel, db: Session) -> Tag | None:
#     tag = db.query(Tag).filter(Tag.id == tag_id).first()
#     if tag:
#         tag .name = body.name
#         db.commit()
#     return tag
#
#
# async def remove_tag(tag_id: int, db: Session)  -> Tag | None:
#     tag = db.query(Tag).filter(Tag.id == tag_id).first()
#     if tag:
#         db.delete(tag)
#         db.commit()
#     return tag
