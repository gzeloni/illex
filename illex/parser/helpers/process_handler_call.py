from typing import Any

from illex.core.registry import registry


def process_handler_call(tag: str, expr_part: str, variables: dict) -> Any:
    """Process a handler call with the given tag and expression"""
    from illex.parser.steps import replace_variables
    if tag in registry:
        # First process variables in the expression part
        processed_expr = replace_variables(expr_part, variables)
        # Then call the handler with the processed expression
        return registry[tag](processed_expr)
    else:
        return f"[Unsupported: {tag}]"
