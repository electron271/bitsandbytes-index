# bitsandbytes-index

Automated index for nightly builds of bitsandbytes.

## Reasoning

- I am working on porting bitsandbytes ROCM to unsloth
- The release version of bitsandbytes is not built with ROCM support
- The nightly builds are in a format that does not follow [Python packaging standards](https://packaging.python.org/en/latest/specifications/binary-distribution-format/), as such `uv` cannot install them

# If bitsandbytes either makes their own index, fixes the wheel format, or builds wheels with ROCM support open an issue.
