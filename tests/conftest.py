import os
import sys

# So that we can do `import forgai in our tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import forgai # noqa: E402

forg.api_base = os.getenv("FORG_API_BASE")  # type: ignore
forg.api_key = os.getenv("FORG_API_KEY")  # type: ignore
