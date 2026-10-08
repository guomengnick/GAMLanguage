"""data/*.csv -> docs/*.md（自動產生，請勿手改 MD）"""
import csv
from pathlib import Path

root = Path(__file__).parent.parent
for src in sorted((root / "data").glob("*.csv")):
    with open(src, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    cell = lambda v: v.replace("|", r"\|").replace(r"\n", "<br>").replace("\n", "<br>").strip()
    head, body = rows[0], rows[1:]
    lines = [f"# {src.stem}", "", f"> 由 `data/{src.name}` 自動產生，請改 CSV 不要改這裡。共 {len(body)} 筆。", "",
             "| " + " | ".join(cell(h) for h in head) + " |",
             "|" + "---|" * len(head)]
    lines += ["| " + " | ".join(cell(v) for v in (r + [""] * len(head))[:len(head)]) + " |" for r in body]
    (root / "docs" / f"{src.stem}.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"docs/{src.stem}.md")
