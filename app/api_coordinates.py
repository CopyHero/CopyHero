from typing import List
from pydantic import BaseModel
from fastapi import Depends
from .app import get_user_info, app
from .utils.utils import calculate_base64_hash  # Utility function to calculate hash
from .db.query_coordinate import QueryCoordinate  # Query class for coordinates
from .lib.paddle_ocr import paddle_ocr_from_base64  # OCR function


# Function to format OCR results into a structured format
def format_coordinates(lines: List[any]):
    data = []
    for line in lines:
        line_points = []
        for i in range(4):
            line_points.append(
                {"x": line[0][i][0], "y": line[0][i][1]}
            )  # Extract points
        words = line[1][0]  # Extract words
        blocks = [{"locations": line_points, "word": words}]
        data.append({"words": words, "line_points": line_points, "blocks": blocks})
    return data


# Request model for the get_coordinates API
class GetCoordinatesRequest(BaseModel):
    image_url: str  # URL of the image
    referrer: str  # Referrer information
    image_data: str  # Base64 encoded image data
    hash: str  # Hash value of the image


# API endpoint to get coordinates from an image
@app.post("/get_coordinates")
def get_coordinates(
    request_data: GetCoordinatesRequest,
    user: dict = Depends(get_user_info),  # Dependency to get user info
):
    if (
        not request_data.hash or not request_data.image_data
    ):  # Check for required fields
        return {"code": 401}

    if request_data.hash:
        words = QueryCoordinate.query_coordinates(
            hash=request_data.hash
        )  # Query coordinates by hash
        if words:
            return {"code": 200, "data": words}  # Return cached words if found

    # Calculate hash from image data and verify it matches the provided hash
    hash = calculate_base64_hash(request_data.image_data)
    if request_data.hash != hash:
        return {"code": 401, "message": "invalid request"}

    # Perform OCR on the base64 image data
    [paddle_data, elapsed_time] = paddle_ocr_from_base64(
        image_base64_data=request_data.image_data
    )
    words = format_coordinates(paddle_data[0])  # Format OCR results

    # Cache the results
    QueryCoordinate.create(hash=hash, words=words, elapsed_time=elapsed_time)
    if words:
        return {"code": 200, "data": words}  # Return words if OCR is successful

    return {"code": 200, "data": []}  # Return empty data if no words are found
