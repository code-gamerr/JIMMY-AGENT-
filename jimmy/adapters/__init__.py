from jimmy.adapters.ecc import EccAdapter
from jimmy.adapters.landing import LandingAdapter
from jimmy.adapters.munder import MunderAdapter
from jimmy.adapters.openclaw import OpenClawAdapter
from jimmy.adapters.research import ResearchAdapter

ADAPTERS = {
    "openclaw": OpenClawAdapter,
    "munder": MunderAdapter,
    "ecc": EccAdapter,
    "landing": LandingAdapter,
    "research": ResearchAdapter,
}


def build_adapters() -> dict:
    return {key: cls() for key, cls in ADAPTERS.items()}
