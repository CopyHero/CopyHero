from .model import Coordinate
import json
from mongoengine import Q


# Define a class for querying and creating Coordinate records
class QueryCoordinate:
    @classmethod
    def query_coordinates(cls, hash: str):
        """
        Query a coordinate record by its hash value.
        If the record is found and has words, return the words as a JSON object.
        """
        record = Coordinate.objects(
            hash=hash
        ).first()  # Find the first record with the matching hash
        if record and record.words:  # Check if the record exists and has words
            return json.loads(record.words)  # Return the words as a JSON object

    @classmethod
    def create(cls, hash: str, words: any, elapsed_time: int):
        """
        Create a new coordinate record if it does not already exist.
        The words are stored as a JSON string.
        """
        record = Coordinate.objects(
            hash=hash
        ).first()  # Find the first record with the matching hash
        if not record:  # If no record is found, create a new one
            record = Coordinate(
                hash=hash,
                words=json.dumps(words),  # Convert words to a JSON string
                elapsed_time=elapsed_time,
            )
            record.save()  # Save the new record
