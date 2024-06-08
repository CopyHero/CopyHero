# coding:utf-8

import datetime

from flask_mongoengine import Document
from mongoengine import *
from mongoengine import connect
from ..settings import logger, settings

# Establish a connection to the MongoDB database
connect(
    settings.database_name,
    host=settings.database_host,
    port=settings.database_port,
    username=settings.database_username,
    password=settings.database_password,
    retryWrites=False,
)


# Define a base document class with common fields and methods
class BaseDocument(Document):
    meta = {
        # "abstract": True,  # Uncomment this line to make the document abstract
        "allow_inheritance": True  # Allow inheritance for this document
    }
    created_at = DateTimeField(
        default=datetime.datetime.utcnow
    )  # Automatically set creation date
    updated_at = DateTimeField()  # Automatically set update date

    @classmethod
    def clean_dict(cls, obj_dict):
        """
        Remove keys that are not part of the document model.
        """
        for item in list(obj_dict.keys()):
            if item not in cls.__dict__:
                del obj_dict[item]
        return obj_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """
        Create an instance from a dictionary, cleaning it first.
        """
        obj_dict = cls.clean_dict(obj_dict)
        return cls._from_son(obj_dict)

    @classmethod
    def upsert(cls, query: dict, data: dict):
        """
        Create or update a document based on the query and data provided.
        """
        try:
            data = cls.clean_dict(data)
            sets = {}
            for key in data.keys():
                sets[f"set__{key}"] = data[key]
            sets["set__updated_at"] = datetime.datetime.utcnow
            return cls.objects(**query).update_one(upsert=True, **sets)
        except Exception as ex:
            logger.error(ex)
            return False


"""
Coordinate module
"""


# Define the Coordinate document class
class Coordinate(Document):
    hash = StringField(required=True)  # Hash field, required
    words = StringField()  # Words field, optional
    elapsed_time = IntField()
    created_at = DateTimeField(
        default=datetime.datetime.utcnow
    )  # Automatically set creation date
    updated_at = DateTimeField(
        default=datetime.datetime.utcnow
    )  # Automatically set update date
    meta = {
        "collection": "coordinate",  # Specify the collection name
        "indexes": [("hash")],  # Create an index on the hash field
    }
