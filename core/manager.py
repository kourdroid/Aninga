import importlib
import pkgutil
import inspect
from typing import Dict, List
import os
import sys

from .plugin import ScraperPlugin

class PluginManager:
    """
    Dynamically loads and manages all scraper plugins found in the sources/ directory.
    This enables adding new sites without ever touching core logic or GUI bindings.
    """
    def __init__(self):
        self.plugins: Dict[str, ScraperPlugin] = {}
        
    def load_plugins(self, package_name: str = "sources"):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        package_dir = os.path.join(base_dir, package_name)
        
        # Ensure sources package exists
        os.makedirs(package_dir, exist_ok=True)
        init_file = os.path.join(package_dir, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, "w", encoding='utf-8') as f: 
                pass
            
        if base_dir not in sys.path:
            sys.path.insert(0, base_dir)
            
        try:
            import sources
        except ImportError as e:
            print(f"[PluginManager] Could not import sources package: {e}")
            return

        for _, mod_name, _ in pkgutil.iter_modules(sources.__path__):
            full_mod_name = f"{package_name}.{mod_name}"
            try:
                mod = importlib.import_module(full_mod_name)
                for name, obj in inspect.getmembers(mod, inspect.isclass):
                    # Only register classes defined within the module itself (no imported classes)
                    if obj.__module__ == full_mod_name:
                        try:
                            instance = obj()
                            # Check structural type conformance to ScraperPlugin protocol
                            if isinstance(instance, ScraperPlugin):
                                self.plugins[instance.name] = instance
                                print(f"[PluginManager] Loaded Plugin: {instance.name}")
                        except Exception as e:
                            print(f"[PluginManager] Error instantiating {name}: {e}")
            except Exception as e:
                print(f"[PluginManager] Error loading module {mod_name}: {e}")

    def get_plugin(self, name: str) -> ScraperPlugin:
        return self.plugins.get(name)

    def get_all_plugins(self) -> List[ScraperPlugin]:
        return list(self.plugins.values())
