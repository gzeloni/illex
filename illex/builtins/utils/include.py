import illex
from illex.decorators.function import function


@function("include")
def handle_include(file_path: str) -> str:
    try:
        if not file_path.endswith('.illex'):
            file_path += '.illex'

        with open(file_path, 'r') as f:
            content = f.read()

        return illex.parse(content, {})
    except FileNotFoundError:
        return f"[Import error: File '{file_path}' not found]"
    except Exception as e:
        return f"[Import error: {str(e)}]"
