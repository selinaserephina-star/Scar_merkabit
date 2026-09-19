"""
build_v2.py — assembles Roof_and_Clock_MATH_v2.md from math_v2_partA.md + math_v2_partB.md
(the mathematics edition: no correspondence history, no dates, no registry numbers in the body),
isolates display equations into their own paragraphs, and renders the .docx with pandoc
(LaTeX math -> native Word equations; '#' headings -> Word Heading 1).

Run from joint_paper/:  python build_v2.py
"""
import re, subprocess, sys, hashlib, pathlib

A = pathlib.Path("math_v2_partA.md").read_text(encoding="utf-8")
B = pathlib.Path("math_v2_partB.md").read_text(encoding="utf-8")
s = A.rstrip("\n") + "\n" + B

# words that must not appear in a mathematics paper's body (the record lives in v1.0)
banned = ["first author", "second author", "Stone ", "SM-0", "registered guess", "on his word",
          "Rule 3", "2026-09", "Selina", "Ilya", "envelope", "registry"]
body = s.split("---", 2)[2].split("# Appendix B.")[0]   # skip the YAML front matter (author names)
for b in banned:
    hits = [m.start() for m in re.finditer(re.escape(b), body)]
    assert not hits, f"banned phrase {b!r} in body at {hits[:3]}: {body[hits[0]-60:hits[0]+60]!r}"
print("banned-phrase check (body): clean")

# isolate display blocks
lines = s.split("\n"); out = []; i = 0; n_disp = 0
while i < len(lines):
    ln = lines[i]
    m = re.match(r"^(\s*\$\$.*?\$\$)(\s*\S.*)$", ln)
    if m:
        lines[i:i + 1] = [m.group(1), m.group(2).lstrip()]; ln = lines[i]
    if re.match(r"^\s*\$\$", ln):
        j = i
        while not lines[j].rstrip().endswith("$$"):
            j += 1
        if out and out[-1].strip() != "": out.append("")
        out.extend(lines[i:j + 1]); n_disp += 1
        if j + 1 < len(lines) and lines[j + 1].strip() != "": out.append("")
        i = j + 1
    else:
        out.append(ln); i += 1
s = "\n".join(out)
print("display equations isolated:", n_disp)

OUT_MD = pathlib.Path("Roof_and_Clock_MATH_v2.md"); OUT_DOCX = pathlib.Path("Roof_and_Clock_MATH_v2.docx")
OUT_MD.write_text(s, encoding="utf-8", newline="\n")
words = len(re.findall(r"\w+", s))
print("wrote", OUT_MD, hashlib.sha256(s.encode()).hexdigest()[:16], len(s), "chars,", s.count("\n"), "lines,", words, "words")

cmd = ["pandoc", str(OUT_MD), "-o", str(OUT_DOCX),
       "--from", "markdown+tex_math_dollars+pipe_tables+yaml_metadata_block+smart"]
r = subprocess.run(cmd, capture_output=True, text=True)
print(" ".join(cmd)); print(r.stdout, r.stderr)
if r.returncode: sys.exit(r.returncode)
print("wrote", OUT_DOCX, OUT_DOCX.stat().st_size, "bytes", hashlib.sha256(OUT_DOCX.read_bytes()).hexdigest()[:16])
