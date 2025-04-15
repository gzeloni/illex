from illex.core.registry import registry


class FunctionLoadException(Exception):
    pass


def function(tag: str):
    def decorator(func):
        func_path = f"{func.__module__}.{func.__name__}"
        registry.update({tag: func_path})
        return func
    return decorator


def load_functions(package_path):
    import importlib.util
    import os
    import sys

    package = importlib.import_module(package_path)
    base_dir = os.path.dirname(package.__file__)
    base_package = package_path

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if not d.startswith('_')]

        rel_path = os.path.relpath(root, base_dir)
        if rel_path == '.':
            current_package = base_package
        else:
            current_package = f"{base_package}.{rel_path.replace(os.path.sep, '.')}"

        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                file_path = os.path.join(root, file)

                module_name = f"{current_package}.{file[:-3]}"

                try:
                    spec = importlib.util.spec_from_file_location(
                        module_name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[module_name] = module
                    spec.loader.exec_module(module)
                except Exception as e:
                    raise FunctionLoadException(f"Error importing {module_name}: {e}")
