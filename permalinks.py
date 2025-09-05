import hashlib
import os
import shutil
import pathlib
import re

path = next(pathlib.Path("bitsandbytes/").rglob("bitsandbytes*manylinux*x86_64.whl"))

with open(path, "rb") as f:
    sha256 = hashlib.sha256(f.read()).hexdigest()
    print(sha256)

if not os.path.exists(f"permalinks/{sha256[:16]}/{path.name}"):
    os.makedirs(f"permalinks/{sha256[:16]}", exist_ok=True)
    print(
        shutil.copy(
            path,
            f"permalinks/{sha256[:16]}/{path.name}",
        )
    )

with open("README.md", "r") as f:
    permalink = f"https://electron271.github.io/bitsandbytes-index/permalinks/{sha256[:16]}/{path.name}#sha256={sha256}"

    readme = f.read()

    begin_tag = "<!-- permalinks.py START -->"
    end_tag = "<!-- permalinks.py END -->"

    readme = (
        readme[: readme.find(begin_tag) + len(begin_tag)]
        + readme[readme.find(end_tag) :]
    )

    output = f"{begin_tag}\n**Permalink**: {permalink}\n"
    readme = readme.replace(begin_tag, output)

    with open("README.md", "w") as f:
        print("characters written: " + str(f.write(readme)))
