"""Resource service proxy router."""

from app.core.config import settings
from .proxy import create_proxy_router

router = create_proxy_router("/resources", settings.RESOURCE_SERVICE_URL, tags=["resources"])
