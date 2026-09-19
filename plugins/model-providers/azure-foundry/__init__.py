"""Microsoft Foundry provider profile.

The endpoint here is the app default. ``model.base_url`` in config.yaml and
``AZURE_FOUNDRY_BASE_URL`` / ``AZURE_OPENAI_ENDPOINT`` still override it.
Change this URL when the Foundry resource changes — the key stays in ``.env``.
"""

from providers import register_provider
from providers.base import ProviderProfile

# Same resource as .azure/jimmy.env.example and the Azure container spec.
AZURE_FOUNDRY_ENDPOINT = "https://medmxlabs-openai.openai.azure.com/openai/v1"

azure_foundry = ProviderProfile(
    name="azure-foundry",
    aliases=("azure", "azure-ai-foundry", "azure-ai"),
    display_name="Azure Foundry",
    description="Microsoft Foundry - OpenAI-compatible endpoint",
    signup_url="https://ai.azure.com/",
    env_vars=("AZURE_FOUNDRY_API_KEY", "AZURE_FOUNDRY_BASE_URL"),
    base_url=AZURE_FOUNDRY_ENDPOINT,
    auth_type="api_key",
)

register_provider(azure_foundry)
