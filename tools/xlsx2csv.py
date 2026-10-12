"""一次性：把 分板機全警報碼.xlsx 第一個工作表轉成 data/alarm-codes.csv（之後改 CSV 就好）"""
import csv, sys
from pathlib import Path
import openpyxl
sys.stdout.reconfigure(encoding="utf-8")   # GitHub Actions 主控台非 UTF-8，印中文會當掉

ws = openpyxl.load_workbook(sys.argv[1], data_only=True).worksheets[0]
rows = [["" if v is None else str(v) for v in r] for r in ws.iter_rows(values_only=True)]
width = max(i + 1 for i, v in enumerate(rows[0]) if v)          # 只留有表頭的欄（右側為輔助公式）
rows = [r[:width] for r in rows if any(r)]
out = Path(__file__).parent.parent / "data" / "alarm-codes.csv"
with open(out, "w", encoding="utf-8-sig", newline="") as f:      # utf-8-sig：Excel 開啟不亂碼
    csv.writer(f, lineterminator="\r\n").writerows(rows)
print(f"{out}: {len(rows) - 1} 筆")
