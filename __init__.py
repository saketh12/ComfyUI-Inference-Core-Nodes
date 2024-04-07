import sys
sys.path.append('/root/custom_nodes/ComfyUI-Inference-Core-Nodes')

from src.inference_core_nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ("NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS")
