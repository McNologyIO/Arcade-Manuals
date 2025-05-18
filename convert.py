import pymupdf4llm
import pathlib

md_text = pymupdf4llm.to_markdown("spinnwin.pdf")
pathlib.Path("spinnwin.md").write_bytes(md_text.encode())