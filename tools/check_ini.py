"""檢查 UTF-16 語言檔沒有被存成其他編碼（存成 UTF-8 時 git 不會報錯，而是把整個檔案變亂碼）
用法：python tools/check_ini.py [檔案...]   不給檔案 = 檢查全部"""
import sys
from pathlib import Path, PurePosixPath
sys.stdout.reconfigure(encoding="utf-8")   # GitHub Actions 主控台非 UTF-8，印中文會當掉

PATTERNS = ("machines/*/Language/*.ini", "machines/*/PLCIni/Name_*.ini")

def is_utf16_path(p: str) -> bool:
    return any(PurePosixPath(p.replace("\\", "/")).match(pat) for pat in PATTERNS)

root = Path(__file__).parent.parent
files = [f for f in sys.argv[1:] if is_utf16_path(f)] or \
        ([] if len(sys.argv) > 1 else [str(p.relative_to(root)) for pat in PATTERNS for p in root.glob(pat)])
bad = []
for f in files:
    p = root / f
    if not p.exists():
        continue                                   # 刪除檔案不用檢查
    data = p.read_bytes()
    ok = data.startswith(b"\xff\xfe")
    if ok:
        text = data[2:].decode("utf-16-le", errors="replace")
        ok = "\ufffd" not in text and sum("=" in line for line in text.splitlines()) >= 2
    if not ok:
        bad.append(f)
if bad:
    print("以下語言檔編碼錯誤，必須存成「UTF-16 LE」（記事本另存新檔 → 編碼選 UTF-16 LE）：")
    print("\n".join("  " + f for f in bad))
    sys.exit(1)
print(f"語言檔編碼檢查通過（{len(files)} 個）")
