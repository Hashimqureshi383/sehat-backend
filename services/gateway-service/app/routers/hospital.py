"""Hospital service proxy router."""

from app.core.config import settings
from .proxy import create_proxy_router

router = create_proxy_router("/hospitals", settings.HOSPITAL_SERVICE_URL, tags=["hospitals"])
