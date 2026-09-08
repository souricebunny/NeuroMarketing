"""Download the standalone tectonic.exe (self-contained LaTeX engine)."""
import json, sys, urllib.request, zipfile, io, pathlib, ssl

DEST = pathlib.Path(".")
API = "https://api.github.com/repos/tectonic-typesetting/tectonic/releases/latest"

ctx = ssl.create_default_context()
req = urllib.request.Request(API, headers={"User-Agent": "tectonic-fetch"})
try:
    data = json.load(urllib.request.urlopen(req, timeout=60, context=ctx))
except Exception as e:
    print("API_FAIL", type(e).__name__, e); sys.exit(2)

asset = None
for a in data.get("assets", []):
    n = a["name"]
    if n.endswith(".zip") and "x86_64-pc-windows-msvc" in n:
        asset = a; break
if not asset:
    print("NO_ASSET", [a["name"] for a in data.get("assets", [])]); sys.exit(3)

print("tag:", data.get("tag_name"), "| asset:", asset["name"])
url = asset["browser_download_url"]
buf = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "tectonic-fetch"}),
                             timeout=300, context=ctx).read()
print("downloaded bytes:", len(buf))
z = zipfile.ZipFile(io.BytesIO(buf))
names = z.namelist()
print("zip contents:", names)
exe = next((m for m in names if m.endswith("tectonic.exe")), None)
if not exe:
    print("NO_EXE_IN_ZIP"); sys.exit(4)
with z.open(exe) as src:
    (DEST / "tectonic.exe").write_bytes(src.read())
print("wrote", (DEST / "tectonic.exe").resolve(), (DEST / "tectonic.exe").stat().st_size, "bytes")
