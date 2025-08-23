"""NGO service proxy router."""

from app.core.config import settings
from .proxy import create_proxy_router

router = create_proxy_router("/ngos", settings.NGO_SERVICE_URL, tags=["ngos"])
