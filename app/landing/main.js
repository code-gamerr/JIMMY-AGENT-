/**
 * Jimmy landing — rebuilt from scratch.
 * Terminal dramatizes real event types / adapters only.
 */
(function () {
  "use strict";

  const AGENTS = ["openclaw", "munder", "ecc", "research", "landing"];

  const SCENES = [
    {
      id: "a7f3c1e902bd",
      agent: "munder",
      goal: "Assign coding work in munder-difflin/",
      lines: [
        { cls: "dim", text: "task.created · queued" },
        { cls: "", text: "task.planning · coding workspace" },
        { cls: "hi", text: "task.routed · agent=munder" },
        { cls: "", text: "command.started · git status" },
        { cls: "ok", text: "command.finished · exit 0" },
        { cls: "ok", text: "experience.stored" },
      ],
      state: ["QUEUED", "PLANNING", "ROUTING", "RUNNING", "RUNNING", "COMPLETED"],
    },
    {
      id: "c21e90ab44d8",
      agent: "ecc",
      goal: "ECC consult via scripts/ecc.js",
      lines: [
        { cls: "dim", text: "task.created" },
        { cls: "hi", text: "task.routed · agent=ecc · cwd=ECC/" },
        { cls: "", text: "command.started · node ECC/scripts/ecc.js consult" },
        { cls: "", text: "command.output · stdout chunk" },
        { cls: "ok", text: "command.finished · duration_ms recorded" },
      ],
      state: ["QUEUED", "ROUTING", "RUNNING", "RUNNING", "COMPLETED"],
    },
    {
      id: "9b08d4e1aa17",
      agent: "openclaw",
      goal: "Probe OpenClaw gateway status",
      lines: [
        { cls: "dim", text: "task.created" },
        { cls: "hi", text: "task.routed · agent=openclaw" },
        { cls: "", text: "command.started · node openclaw.mjs gateway status" },
        { cls: "dim", text: "stderr preserved if Node gate fails — no fake success" },
        { cls: "ok", text: "task.completed · probe logged" },
      ],
      state: ["QUEUED", "ROUTING", "RUNNING", "RUNNING", "COMPLETED"],
    },
  ];

  const logEl = document.getElementById("tlog");
  const tid = document.getElementById("tid");
  const tstate = document.getElementById("tstate");
  const tgoal = document.getElementById("tgoal");
  const agentsBar = document.getElementById("agentsBar");
  const copyBtn = document.getElementById("copy");
  const cmd = document.getElementById("cmd");
  const canvas = document.getElementById("bg");
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Agent chips
  if (agentsBar) {
    agentsBar.innerHTML = AGENTS.map((a) => `<span data-a="${a}">${a}</span>`).join("");
  }

  function setAgent(name) {
    if (!agentsBar) return;
    agentsBar.querySelectorAll("span").forEach((el) => {
      el.classList.toggle("on", el.getAttribute("data-a") === name);
    });
  }

  function stamp() {
    const d = new Date();
    return [d.getHours(), d.getMinutes(), d.getSeconds()]
      .map((n) => String(n).padStart(2, "0"))
      .join(":");
  }

  let scene = 0;
  let step = 0;
  let visible = true;
  let timer = null;

  function begin(i) {
    const s = SCENES[i % SCENES.length];
    scene = i % SCENES.length;
    step = 0;
    if (logEl) logEl.textContent = "";
    if (tid) tid.textContent = `task · ${s.id}`;
    if (tgoal) tgoal.textContent = s.goal;
    if (tstate) tstate.textContent = "QUEUED";
    setAgent(s.agent);
  }

  function tick() {
    if (!visible && !reduced) return;
    const s = SCENES[scene];
    if (step >= s.lines.length) {
      begin(scene + 1);
      return;
    }
    const line = s.lines[step];
    const st = s.state[step] || "RUNNING";
    if (tstate) tstate.textContent = st;
    if (logEl) {
      const row = document.createElement("div");
      row.className = line.cls || "";
      row.textContent = `${stamp()}  ${line.text}`;
      logEl.appendChild(row);
      while (logEl.childNodes.length > 8) logEl.removeChild(logEl.firstChild);
    }
    step += 1;
  }

  function startDemo() {
    begin(0);
    if (reduced) {
      SCENES[0].lines.forEach((line, i) => {
        if (tstate) tstate.textContent = SCENES[0].state[i];
        if (logEl) {
          const row = document.createElement("div");
          row.className = line.cls || "";
          row.textContent = `00:00:0${i}  ${line.text}`;
          logEl.appendChild(row);
        }
      });
      setAgent(SCENES[0].agent);
      return;
    }
    tick();
    timer = window.setInterval(tick, 1000);
  }

  const term = document.getElementById("terminal");
  if (term && "IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        visible = entries.some((e) => e.isIntersecting);
      },
      { threshold: 0.2 }
    );
    io.observe(term);
  }

  if (copyBtn && cmd) {
    copyBtn.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(cmd.textContent.trim());
        copyBtn.textContent = "Copied";
        window.setTimeout(() => {
          copyBtn.textContent = "Copy";
        }, 1200);
      } catch {
        copyBtn.textContent = "Failed";
      }
    });
  }

  // Soft particle field (compositor-friendly)
  function initBg() {
    if (!canvas || reduced) return;
    const ctx = canvas.getContext("2d", { alpha: true });
    if (!ctx) return;

    let w = 0;
    let h = 0;
    let raf = 0;
    const dots = Array.from({ length: 48 }, () => ({
      x: Math.random(),
      y: Math.random(),
      r: 0.4 + Math.random() * 1.4,
      v: 0.00015 + Math.random() * 0.00035,
    }));

    function resize() {
      w = canvas.width = window.innerWidth * devicePixelRatio;
      h = canvas.height = window.innerHeight * devicePixelRatio;
      canvas.style.width = `${window.innerWidth}px`;
      canvas.style.height = `${window.innerHeight}px`;
      ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
    }

    function frame() {
      const vw = window.innerWidth;
      const vh = window.innerHeight;
      ctx.clearRect(0, 0, vw, vh);
      const g = ctx.createRadialGradient(vw * 0.2, vh * 0.1, 0, vw * 0.2, vh * 0.1, vw * 0.55);
      g.addColorStop(0, "rgba(110,243,197,0.07)");
      g.addColorStop(1, "rgba(0,0,0,0)");
      ctx.fillStyle = g;
      ctx.fillRect(0, 0, vw, vh);

      ctx.fillStyle = "rgba(237,241,245,0.35)";
      for (const d of dots) {
        d.y -= d.v;
        if (d.y < -0.02) d.y = 1.02;
        ctx.beginPath();
        ctx.arc(d.x * vw, d.y * vh, d.r, 0, Math.PI * 2);
        ctx.fill();
      }
      raf = requestAnimationFrame(frame);
    }

    resize();
    window.addEventListener("resize", resize, { passive: true });
    frame();

    document.addEventListener("visibilitychange", () => {
      if (document.hidden) cancelAnimationFrame(raf);
      else frame();
    });
  }

  startDemo();
  initBg();
})();
