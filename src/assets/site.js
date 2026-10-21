/* zero-index ต้นแบบเว็บเอกสาร เขียนเองทั้งหมด ไม่ใช้ไลบรารี */
(function () {
  "use strict";

  var root = document.documentElement;
  var THEME_KEY = "zi-theme";
  var darkQuery = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $all(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }

  /* ---------- โหมดมืด ---------- */

  function effectiveTheme() {
    var t = root.getAttribute("data-theme");
    if (t === "light" || t === "dark") return t;
    return darkQuery && darkQuery.matches ? "dark" : "light";
  }

  function syncThemeButton() {
    var btn = $(".theme-btn");
    if (!btn) return;
    var label = effectiveTheme() === "dark" ? "เปลี่ยนเป็นโหมดสว่าง" : "เปลี่ยนเป็นโหมดมืด";
    btn.setAttribute("aria-label", label);
    btn.setAttribute("title", label);
  }

  function initTheme() {
    var btn = $(".theme-btn");
    if (!btn) return;
    syncThemeButton();
    btn.addEventListener("click", function () {
      var next = effectiveTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem(THEME_KEY, next); } catch (e) { /* ไม่มีที่เก็บก็ยังสลับได้ */ }
      syncThemeButton();
    });
    if (darkQuery) {
      var onChange = function () { syncThemeButton(); };
      if (darkQuery.addEventListener) darkQuery.addEventListener("change", onChange);
      else if (darkQuery.addListener) darkQuery.addListener(onChange);
    }
  }

  /* ---------- เมนูบนจอแคบ ---------- */

  function initDrawer() {
    var body = document.body;
    var openBtn = $(".menu-btn");
    var closeBtn = $(".drawer-close");
    var scrim = $(".scrim");
    if (!openBtn) return;

    function setOpen(open) {
      body.classList.toggle("nav-open", open);
      openBtn.setAttribute("aria-expanded", open ? "true" : "false");
      if (open) {
        var current = $('.sidebar a[aria-current="page"]') || $(".sidebar a");
        if (current) current.focus({ preventScroll: true });
      }
    }

    openBtn.addEventListener("click", function () { setOpen(!body.classList.contains("nav-open")); });
    if (closeBtn) closeBtn.addEventListener("click", function () { setOpen(false); openBtn.focus(); });
    if (scrim) scrim.addEventListener("click", function () { setOpen(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && body.classList.contains("nav-open")) { setOpen(false); openBtn.focus(); }
    });
    $all(".sidebar a").forEach(function (a) {
      a.addEventListener("click", function () { setOpen(false); });
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth >= 960 && body.classList.contains("nav-open")) setOpen(false);
    });
  }

  /* ---------- สีไวยากรณ์ภาษา C ---------- */

  var C_TYPES = /^(int|char|void|float|double|long|short|unsigned|signed|bool|size_t|FILE)$/;
  var C_KEYWORDS = /^(auto|break|case|const|continue|default|do|else|enum|extern|for|goto|if|inline|register|return|sizeof|static|struct|switch|typedef|union|volatile|while)$/;

  function tk(cls, text) { return '<span class="tk-' + cls + '">' + esc(text) + "</span>"; }

  function hlString(s) {
    var out = "", last = 0, re = /\\./g, m;
    while ((m = re.exec(s))) {
      out += esc(s.slice(last, m.index)) + '<span class="tk-esc">' + esc(m[0]) + "</span>";
      last = m.index + m[0].length;
    }
    return '<span class="tk-str">' + out + esc(s.slice(last)) + "</span>";
  }

  /* คืนค่า { html, anno } โดย anno คือเลขคำอธิบาย ถ้าบรรทัดนี้มี // (n)! */
  function hlCodeC(s) {
    var re = /(\/\/.*$)|("(?:\\.|[^"\\])*")|('(?:\\.|[^'\\])*')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_]\w*)|(\s+)|([\s\S])/g;
    var out = "", m, anno = null;
    while ((m = re.exec(s))) {
      if (m[1]) {
        var a = m[1].match(/^\/\/\s*\((\d+)\)!\s*$/);
        if (a) { anno = a[1]; out += "\u0000ANNO\u0000"; }
        else out += tk("com", m[1]);
      } else if (m[2]) out += hlString(m[2]);
      else if (m[3]) out += hlString(m[3]);
      else if (m[4]) out += tk("num", m[4]);
      else if (m[5]) {
        var w = m[5];
        if (C_TYPES.test(w)) out += tk("type", w);
        else if (C_KEYWORDS.test(w)) out += tk("kw", w);
        else if (/^\s*\(/.test(s.slice(re.lastIndex))) out += tk("fn", w);
        else out += esc(w);
      } else out += esc(m[0]);
    }
    return { html: out, anno: anno };
  }

  function hlLineC(line) {
    var pre = line.match(/^(\s*)(#\s*\w+)(.*)$/);
    if (!pre) return hlCodeC(line);
    var head = esc(pre[1]) + tk("pre", pre[2]);
    var rest = pre[3];
    var hdr = rest.match(/^(\s*)(<[^>]*>)(.*)$/);
    if (hdr) { head += esc(hdr[1]) + tk("hdr", hdr[2]); rest = hdr[3]; }
    var r = hlCodeC(rest);
    return { html: head + r.html, anno: r.anno };
  }

  /* ---------- สีข้อความจาก gcc ---------- */

  /* บรรทัดที่มีเลขหน้า | คือโค้ดของเรา บรรทัด | ที่ไม่มีเลขคือ ^ ชี้จุดผิด หรือคำแนะนำให้แก้ */
  function hlGcc(line) {
    var m = line.match(/^((?:\S.*?:(?:\d+:\d+:)?)?)(\s*)(error|warning|note)(:)(.*)$/);
    if (m) return (m[1] ? tk("loc", m[1]) : "") + esc(m[2]) + tk("sev-" + m[3], m[3] + m[4]) + esc(m[5]);
    m = line.match(/^(\s*(?:\d+|\+\+\+)?\s*)\|(.*)$/);
    if (m) {
      var gutter = tk("gutter", m[1] + "|");
      if (/\d/.test(m[1])) return gutter + esc(m[2]);
      if (/^\s*[\^~]+\s*$/.test(m[2])) return gutter + tk("caret", m[2]);
      if (/\S/.test(m[2])) return gutter + tk("fix", m[2]);
      return gutter + esc(m[2]);
    }
    m = line.match(/^(\S+?\.exe:)(.*)$/);
    if (m) return tk("loc", m[1]) + esc(m[2]);
    return esc(line);
  }

  var ICON_COPY = '<svg class="i-copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v1"/></svg>';
  var ICON_CHECK = '<svg class="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>';

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand("copy") ? resolve() : reject(); } catch (e) { reject(e); }
      document.body.removeChild(ta);
    });
  }

  function initCode() {
    $all(".code").forEach(function (block) {
      var codeEl = $("code", block);
      if (!codeEl) return;
      var lang = block.getAttribute("data-lang") || "text";
      var raw = codeEl.textContent.replace(/\n$/, "");
      var lines = raw.split("\n");
      var annoLines = {};
      var cleanLines = [];

      var html = lines.map(function (line) {
        var inner;
        if (lang === "gcc") {
          inner = hlGcc(line);
          cleanLines.push(line);
        } else if (lang === "c") {
          var r = hlLineC(line);
          inner = r.html;
          if (r.anno) {
            annoLines[r.anno] = true;
            inner = inner.replace("\u0000ANNO\u0000",
              '<button type="button" class="anno-btn" data-anno="' + r.anno + '" aria-expanded="false" aria-label="คำอธิบายข้อ ' + r.anno + '">' + r.anno + "</button>");
            cleanLines.push(line.replace(/\s*\/\/\s*\(\d+\)!\s*$/, ""));
          } else cleanLines.push(line);
        } else {
          inner = esc(line);
          cleanLines.push(line);
        }
        return '<span class="ln">' + inner + "</span>";
      }).join("\n");

      codeEl.innerHTML = html;

      /* ผลลัพธ์จากโปรแกรมไม่มีอะไรให้คัดลอกไปใช้ */
      if (lang === "output") return;

      var copyBtn = document.createElement("button");
      copyBtn.type = "button";
      copyBtn.className = "copy-btn";
      copyBtn.setAttribute("aria-label", "คัดลอกโค้ด");
      copyBtn.setAttribute("title", "คัดลอกโค้ด");
      copyBtn.innerHTML = ICON_COPY + ICON_CHECK;
      var cleanText = cleanLines.join("\n") + "\n";
      copyBtn.addEventListener("click", function () {
        copyText(cleanText).then(function () {
          copyBtn.classList.add("is-done");
          copyBtn.setAttribute("title", "คัดลอกแล้ว");
          setTimeout(function () {
            copyBtn.classList.remove("is-done");
            copyBtn.setAttribute("title", "คัดลอกโค้ด");
          }, 1600);
        }, function () { /* คัดลอกไม่ได้ ปล่อยให้เลือกข้อความเอง */ });
      });
      block.appendChild(copyBtn);

      if (block.hasAttribute("data-annotate")) initAnnotations(block);
    });
  }

  /* ---------- คำอธิบายโค้ดแบบวงกลมตัวเลข ---------- */

  var openAnno = null;

  function closeAnno() {
    if (!openAnno) return;
    openAnno.btn.setAttribute("aria-expanded", "false");
    openAnno.pop.hidden = true;
    openAnno = null;
  }

  function placePop(block, btn, pop) {
    var b = btn.getBoundingClientRect();
    var w = block.getBoundingClientRect();
    var popW = pop.offsetWidth;
    var left = b.left - w.left - 14;
    left = Math.max(8, Math.min(left, w.width - popW - 8));
    pop.style.left = left + "px";
    pop.style.top = (b.bottom - w.top + 8) + "px";
  }

  function initAnnotations(block) {
    var list = block.nextElementSibling;
    if (!list || !list.classList.contains("anno-list")) return;
    var items = $all(":scope > li", list);
    var pop = document.createElement("div");
    pop.className = "anno-pop";
    pop.hidden = true;
    pop.id = "anno-pop-" + Math.random().toString(36).slice(2, 8);
    pop.setAttribute("role", "note");
    block.appendChild(pop);
    list.hidden = true;

    $all(".anno-btn", block).forEach(function (btn) {
      btn.setAttribute("aria-controls", pop.id);
      btn.addEventListener("click", function (e) {
        e.stopPropagation();
        var same = openAnno && openAnno.btn === btn;
        closeAnno();
        if (same) return;
        var item = items[parseInt(btn.getAttribute("data-anno"), 10) - 1];
        if (!item) return;
        pop.innerHTML = item.innerHTML;
        pop.hidden = false;
        btn.setAttribute("aria-expanded", "true");
        placePop(block, btn, pop);
        openAnno = { btn: btn, pop: pop, block: block };
      });
    });

    var pre = $("pre", block);
    if (pre) pre.addEventListener("scroll", closeAnno);
    pop.addEventListener("click", function (e) { e.stopPropagation(); });
  }

  function initAnnoGlobal() {
    document.addEventListener("click", closeAnno);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && openAnno) { var b = openAnno.btn; closeAnno(); b.focus(); }
    });
    window.addEventListener("resize", function () {
      if (openAnno) placePop(openAnno.block, openAnno.btn, openAnno.pop);
    });
  }

  /* ---------- สารบัญในหน้า และไฮไลต์ขณะเลื่อน ---------- */

  function initToc() {
    var headings = $all(".doc h2[id], .doc h3[id]");
    var tocList = $("#toc-list");
    var inline = $(".toc-inline");
    var toc = $(".toc");

    headings.forEach(function (h) {
      var a = document.createElement("a");
      a.className = "anchor";
      a.href = "#" + h.id;
      a.setAttribute("aria-label", "ลิงก์มาที่หัวข้อนี้");
      a.textContent = "#";
      h.appendChild(a);
    });

    if (!headings.length) {
      if (toc) toc.style.visibility = "hidden";
      return;
    }

    function title(h) {
      var clone = h.cloneNode(true);
      $all(".anchor", clone).forEach(function (n) { n.remove(); });
      return clone.textContent.trim();
    }

    function build(ul) {
      if (!ul) return [];
      return headings.map(function (h) {
        var li = document.createElement("li");
        var a = document.createElement("a");
        a.href = "#" + h.id;
        a.textContent = title(h);
        a.className = h.tagName === "H3" ? "lvl-3" : "lvl-2";
        li.appendChild(a);
        ul.appendChild(li);
        return a;
      });
    }

    var linksA = build(tocList);
    var linksB = build(inline);
    var activeIdx = -1;

    function update() {
      var offset = 90 + 24;
      var idx = 0;
      for (var i = 0; i < headings.length; i++) {
        if (headings[i].getBoundingClientRect().top - offset <= 0) idx = i;
        else break;
      }
      if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2) {
        idx = headings.length - 1;
      }
      if (idx === activeIdx) return;
      activeIdx = idx;
      [linksA, linksB].forEach(function (links) {
        links.forEach(function (a, i) { a.classList.toggle("is-active", i === idx); });
      });
      var act = linksA[idx];
      if (act && toc && toc.offsetParent !== null) {
        var r = act.getBoundingClientRect(), tr = toc.getBoundingClientRect();
        if (r.top < tr.top || r.bottom > tr.bottom) act.scrollIntoView({ block: "nearest" });
      }
    }

    var ticking = false;
    window.addEventListener("scroll", function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () { ticking = false; update(); });
    }, { passive: true });
    window.addEventListener("resize", update);
    update();
  }

  document.addEventListener("DOMContentLoaded", function () {
    initTheme();
    initDrawer();
    initCode();
    initAnnoGlobal();
    initToc();
  });
})();
