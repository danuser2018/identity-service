from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.api.routes import router

def create_app() -> FastAPI:
    """
    Factory function to initialize and configure the FastAPI application.
    """
    app = FastAPI(
        title="Nova Identity Service",
        description="Servicio de identidad para Nova (MVP)",
        version="1.0.0"
    )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return JSONResponse(
            status_code=400,
            content={"detail": exc.errors()}
        )

    # Include the main router
    app.include_router(router)

    return app
