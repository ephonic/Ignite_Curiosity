# -*- coding: utf-8 -*-
"""将 literal.md 提纲 + chapters/chNNN.md 正文合成为 LaTeX 书籍源文件。"""
import os
import re

SRC = "literal.md"
DST = "literal_book.tex"

# ---------- 行内处理 ----------

def esc(s: str) -> str:
    s = s.replace("\\", "\\textbackslash{}")
    for a, b in [("&", "\\&"), ("%", "\\%"), ("$", "\\$"), ("#", "\\#"),
                 ("_", "\\_"), ("{", "\\{"), ("}", "\\}"),
                 ("~", "\\textasciitilde{}"), ("^", "\\textasciicircum{}")]:
        s = s.replace(a, b)
    s = s.replace("→", "$\\rightarrow$")
    return s

def inline(s: str) -> str:
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", s)
    return s

# ---------- Markdown 块级转换 ----------

class Conv:
    def __init__(self, heading_handler):
        self.out = []
        self.itemize = False
        self.enumerate = False
        self.table = []
        self.heading_handler = heading_handler  # (level, text) -> str or None

    def close_lists(self):
        if self.itemize:
            self.out.append("\\end{itemize}")
            self.itemize = False
        if self.enumerate:
            self.out.append("\\end{enumerate}")
            self.enumerate = False

    def flush_table(self):
        if not self.table:
            return
        rows = []
        for line in self.table:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue
            rows.append(cells)
        self.table = []
        if not rows:
            return
        ncol = max(len(r) for r in rows)
        spec = "l" * (ncol - 1) + "X" if ncol > 1 else "X"
        self.out.append("\\begin{tabularx}{\\linewidth}{%s}" % spec)
        self.out.append("\\toprule")
        for i, r in enumerate(rows):
            r = r + [""] * (ncol - len(r))
            self.out.append(" & ".join(inline(c) for c in r) + " \\\\")
            if i == 0:
                self.out.append("\\midrule")
        self.out.append("\\bottomrule")
        self.out.append("\\end{tabularx}")

    def feed(self, lines):
        i = 0
        while i < len(lines):
            line = lines[i].rstrip()
            i += 1

            if not line.strip():
                self.close_lists()
                self.flush_table()
                continue

            if re.fullmatch(r"-{3,}", line.strip()):
                self.close_lists()
                self.flush_table()
                continue

            if line.lstrip().startswith("|"):
                self.close_lists()
                self.table.append(line)
                continue
            else:
                self.flush_table()

            if line.lstrip().startswith(">"):
                self.close_lists()
                quote = []
                while True:
                    quote.append(line.lstrip()[1:].strip())
                    if i >= len(lines) or not lines[i].lstrip().startswith(">"):
                        break
                    line = lines[i].rstrip()
                    i += 1
                self.out.append("\\begin{quote}")
                self.out.append(inline(" ".join(quote)))
                self.out.append("\\end{quote}")
                continue

            m = re.match(r"^(#{1,6})\s+(.*)$", line)
            if m:
                self.close_lists()
                res = self.heading_handler(len(m.group(1)), m.group(2).strip())
                if res:
                    self.out.append(res)
                continue

            mb = re.match(r"^[-*]\s+(.*)$", line)
            if mb:
                if self.enumerate:
                    self.close_lists()
                if not self.itemize:
                    self.out.append("\\begin{itemize}")
                    self.itemize = True
                self.out.append("\\item " + inline(mb.group(1)))
                continue

            mo = re.match(r"^\d+\.\s+(.*)$", line)
            if mo:
                if self.itemize:
                    self.close_lists()
                if not self.enumerate:
                    self.out.append("\\begin{enumerate}")
                    self.enumerate = True
                self.out.append("\\item " + inline(mo.group(1)))
                continue

            self.close_lists()
            self.out.append(inline(line))
            self.out.append("")

    def finish(self):
        self.close_lists()
        self.flush_table()
        return "\n".join(self.out)

# ---------- 章节正文 ----------

def load_chapter(n):
    path = "chapters/ch%03d.md" % n
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    # 跳过文件自身的 H1 标题
    if lines and re.match(r"^#\s+", lines[0]):
        lines = lines[1:]

    def hh(level, text):
        if level == 2:
            return "\\section{%s}" % inline(text)
        if level == 3:
            return "\\subsection{%s}" % inline(text)
        return "\\subsection*{%s}" % inline(text)

    c = Conv(hh)
    c.feed(lines)
    return c.finish()

# ---------- 主文档（提纲骨架） ----------

def main():
    with open(SRC, encoding="utf-8") as f:
        lines = f.read().splitlines()

    state = {"in_main": False, "in_back": False, "n_chap": 0,
             "with_prose": 0, "skip_outline": False}

    def hh(level, text):
        if level == 1 and re.match(r"^《", text):
            return None  # 书名行
        if level == 1 and re.match(r"^第[一二三]册", text):
            state["skip_outline"] = False
            pre = ""
            if not state["in_main"]:
                state["in_main"] = True
                pre = "\\mainmatter\n"
            return pre + "\\volumediv{%s}" % inline(text)
        if level == 2 and re.match(r"^第.+篇", text):
            state["skip_outline"] = False
            body = re.sub(r"^第.+篇[　 ]*", "", text)
            return "\\part{%s}" % inline(body)
        if level == 2:
            state["skip_outline"] = False
            pre = ""
            if re.match(r"^[四五六七八九十]+、", text) and not state["in_back"]:
                state["in_back"] = True
                pre = "\\backmatter\n"
            return pre + "\\frontchapter{%s}" % inline(text)
        if level == 3:
            mc = re.match(r"^第\s*(\d+)\s*章[　 ]*(.*)$", text)
            if mc:
                n = int(mc.group(1))
                state["n_chap"] += 1
                prose = load_chapter(n)
                if prose is not None:
                    state["with_prose"] += 1
                    state["skip_outline"] = True
                    return "\\chapter{%s}\n%s" % (inline(mc.group(2)), prose)
                state["skip_outline"] = False
                return "\\chapter{%s}" % inline(mc.group(2))
            return "\\section*{%s}" % inline(text)
        return None

    # Conv 不直接支持“跳过大纲行”，这里先预处理：删除有正文章节的大纲要点
    processed = []
    skipping = False
    chap_re = re.compile(r"^### 第\s*(\d+)\s*章")
    for line in lines:
        mh = re.match(r"^(#{1,3})\s", line)
        if mh:
            mc = chap_re.match(line)
            if mc and os.path.exists("chapters/ch%03d.md" % int(mc.group(1))):
                skipping = True
            else:
                skipping = False
            processed.append(line)
            continue
        if skipping:
            continue
        processed.append(line)

    c = Conv(hh)
    c.feed(processed)
    body = c.finish()

    tex = r"""\documentclass[UTF8,fontset=fandol,zihao=-4,openany]{ctexbook}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage[unicode,hidelinks]{hyperref}

\ctexset{
  chapter/name = {第,章},
  chapter/number = \arabic{chapter},
  part/name = {第,篇},
  part/number = \chinese{part},
}

% 分册扉页
\newcommand{\volumediv}[1]{%
  \cleardoublepage
  \thispagestyle{empty}%
  \vspace*{\fill}
  {\centering\zihao{0}\bfseries #1\par}
  \vspace*{\fill}
  \phantomsection
  \addcontentsline{toc}{part}{#1}
  \cleardoublepage
}

% 前言/后记中的不编号章
\newcommand{\frontchapter}[1]{%
  \chapter*{#1}%
  \phantomsection
  \addcontentsline{toc}{chapter}{#1}%
  \markboth{#1}{#1}%
}

\title{\zihao{0}\bfseries 烧掉文科书\\[0.5em] \zihao{2}\mdseries ——初中生的博雅书}
\author{}
\date{}

\begin{document}

\frontmatter
\maketitle

\thispagestyle{empty}
\vspace*{\fill}
\begin{quote}\itshape
人为什么说话、讲故事、相信神圣、追问真理、建立国家、发动革命，又为什么会被一首诗、一座废墟或一段旋律打动？
\end{quote}
\vspace*{\fill}
\cleardoublepage

\tableofcontents
\cleardoublepage

""" + body + r"""

\end{document}
"""
    with open(DST, "w", encoding="utf-8") as f:
        f.write(tex)
    print("章节数: %d，其中含正文: %d" % (state["n_chap"], state["with_prose"]))

if __name__ == "__main__":
    main()
