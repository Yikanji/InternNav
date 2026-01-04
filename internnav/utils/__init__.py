from .comm_utils.client import AgentClient

# Server utilities depend on FastAPI; keep optional for inference-only installs.
try:
	from .comm_utils.server import AgentServer
except Exception:  # pragma: no cover
	AgentServer = None
