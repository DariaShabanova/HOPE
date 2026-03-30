from fastapi import APIRouter, status

router = APIRouter(prefix="/index")

@router.get(status_code= status.HTTP_200_OK, path="")
def GetIndex():
    return {"success": True}


