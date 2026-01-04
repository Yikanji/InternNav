from internnav.agent.base import Agent
from internnav.agent.internvla_n1_agent import InternVLAN1Agent

# Optional agents may require extra dependencies (e.g., FastAPI, Habitat, etc.).
# Keep imports best-effort so that inference-only setups don't fail at import time.
try:
    from internnav.agent.cma_agent import CmaAgent
except Exception:  # pragma: no cover
    CmaAgent = None

try:
    from internnav.agent.rdp_agent import RdpAgent
except Exception:  # pragma: no cover
    RdpAgent = None

try:
    from internnav.agent.seq2seq_agent import Seq2SeqAgent
except Exception:  # pragma: no cover
    Seq2SeqAgent = None

__all__ = [
    'Agent',
    'CmaAgent',
    'RdpAgent',
    'Seq2SeqAgent',
    'InternVLAN1Agent'
]
