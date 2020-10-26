from fastapi import FastAPI

from .middleware import configure_db
from .endpoints import user, auth, resource
from .db import bootstrap

app = FastAPI()

configure_db(app)
bootstrap()

app.include_router(user.router, prefix="/users")
app.include_router(auth.router)
app.include_router(resource.router, prefix="/resource")
