import { FormEvent, useEffect, useState } from "react";

const WAITLIST_KEY = "jimmy-coming-soon-waitlist";

type WaitlistPayload = {
  name: string;
  email: string;
  surface: string;
  at: number;
};

function useScrolled(threshold = 8) {
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > threshold);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, [threshold]);
  return scrolled;
}

function WaitlistForm() {
  const [done, setDone] = useState<WaitlistPayload | null>(() => {
    try {
      const raw = localStorage.getItem(WAITLIST_KEY);
      return raw ? (JSON.parse(raw) as WaitlistPayload) : null;
    } catch {
      return null;
    }
  });

  function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const fd = new FormData(e.currentTarget);
    const name = String(fd.get("name") || "").trim();
    const email = String(fd.get("email") || "").trim();
    const surface = String(fd.get("surface") || "").trim();
    if (!name || !email) return;
    const payload: WaitlistPayload = { name, email, surface, at: Date.now() };
    localStorage.setItem(WAITLIST_KEY, JSON.stringify(payload));
    setDone(payload);
  }

  if (done) {
    return (
      <p className="form-ok" role="status">
        Saved for {done.email}. Nothing leaves this browser yet.
      </p>
    );
  }

  return (
    <form className="form" onSubmit={onSubmit}>
      <div className="form-row">
        <div className="field">
          <label htmlFor="name">Name</label>
          <input id="name" name="name" required autoComplete="name" placeholder="Ada" />
        </div>
        <div className="field">
          <label htmlFor="email">Email</label>
          <input
            id="email"
            name="email"
            type="email"
            required
            autoComplete="email"
            placeholder="you@example.com"
          />
        </div>
      </div>
      <div className="field">
        <label htmlFor="surface">Primary surface</label>
        <input
          id="surface"
          name="surface"
          list="surfaces"
          placeholder="Laptop · Phone · Cloud · Watch"
        />
        <datalist id="surfaces">
          <option value="Laptop" />
          <option value="Phone" />
          <option value="Cloud" />
          <option value="Watch" />
          <option value="All of them" />
        </datalist>
      </div>
      <button className="btn btn-solid" type="submit" style={{ justifySelf: "start" }}>
        Request launch access
      </button>
    </form>
  );
}

export default function App() {
  const scrolled = useScrolled();

  return (
    <div className="app">
      <div className="pixel-field" aria-hidden="true" />

      <header className={`top${scrolled ? " is-scrolled" : ""}`}>
        <a className="brand" href="#top">
          <span className="brand-mark" aria-hidden="true" />
          Jimmy
        </a>
        <nav className="nav" aria-label="Primary">
          <a href="#ecosystem">Ecosystem</a>
          <a href="#method">Method</a>
          <a href="#surfaces">Surfaces</a>
          <a className="nav-cta" href="#join">
            Join
          </a>
        </nav>
      </header>

      <div className="announce">
        <a href="#join">Coming soon — laptop ↔ phone ↔ cloud ↔ watch. Join the waitlist →</a>
      </div>

      <main id="top">
        <section className="hero">
          <div className="hero-stage">
            <h1 className="hero-word">Jimmy</h1>
            <p className="hero-sub">
              Beautiful, fun &amp; agentic OS — one agent across every device you already use.
            </p>
            <div className="hero-actions">
              <a className="btn btn-solid" href="#join">
                Get Jimmy
              </a>
              <a className="btn" href="#ecosystem">
                See the loop
              </a>
            </div>
          </div>

          <div className="hero-dock">
            <aside className="player" aria-label="Status">
              <div className="player-art" aria-hidden="true" />
              <div className="player-meta">
                <p className="player-title">Coming soon</p>
                <p className="player-artist">Personal agentic OS</p>
              </div>
            </aside>
            <p className="hero-foot">Personal, connected &amp; agentic — by you.</p>
          </div>
        </section>

        <section className="section" id="ecosystem">
          <div className="wrap">
            <p className="section-kicker">01 · The ecosystem</p>
            <h2>The malleable OS for the age of agents.</h2>
            <p className="lede">
              Not four apps. One continuous agent that moves with you — desk power on the laptop,
              messages on the phone, memory in the cloud, pulse on the watch.
            </p>
            <div className="grid-4">
              <article className="card">
                <p className="num">01 · Laptop</p>
                <h3>Desk power</h3>
                <p>Terminal, browser, files, desktop control. Where Jimmy can actually run the machine.</p>
              </article>
              <article className="card">
                <p className="num">02 · Phone</p>
                <h3>On the move</h3>
                <p>Same agent in Telegram, Discord, Slack, and more. Voice in, replies out.</p>
              </article>
              <article className="card">
                <p className="num">03 · Cloud</p>
                <h3>Always awake</h3>
                <p>Memory, cron, skills, gateway stay live when your laptop sleeps.</p>
              </article>
              <article className="card">
                <p className="num">04 · Watch</p>
                <h3>Pulse</h3>
                <p>Glanceable status, nudges, approvals — lightest edge of full context.</p>
              </article>
            </div>
          </div>
        </section>

        <section className="section" id="method">
          <div className="wrap">
            <p className="section-kicker">02 · The method</p>
            <h2>We can sync everything.</h2>
            <p className="lede">
              Carry context, act on the surface you’re on, sync through the cloud. Omakase defaults —
              your computer stays yours.
            </p>
            <div className="split">
              <div className="split-visual">
                <img
                  src="/assets/brand/desk-loop.png"
                  alt="Jimmy at the desk connected to phone, watch, and cloud"
                  width={1600}
                  height={900}
                  loading="lazy"
                />
              </div>
              <div className="steps">
                <article className="step">
                  <div className="step-i">01</div>
                  <div>
                    <h3>Carry context</h3>
                    <p>Memory and skills travel with the agent. Start on laptop; finish on phone.</p>
                  </div>
                </article>
                <article className="step">
                  <div className="step-i">02</div>
                  <div>
                    <h3>Act on the surface</h3>
                    <p>CLI and desktop for heavy work. Messaging for rooms you live in. Watch for signal.</p>
                  </div>
                </article>
                <article className="step">
                  <div className="step-i">03</div>
                  <div>
                    <h3>Sync through cloud</h3>
                    <p>Gateway, cron, curated memory — one identity, not four siloed bots.</p>
                  </div>
                </article>
              </div>
            </div>
          </div>
        </section>

        <section className="section" id="surfaces">
          <div className="wrap">
            <p className="section-kicker">03 · The surfaces</p>
            <h2>The agentic OS for the age of agents.</h2>
            <p className="lede">
              Same core on every edge. Extend with skills and plugins — don’t grow a different product
              per device.
            </p>
            <div className="grid-3">
              <article className="tile">
                <span className="tag">CLI · TUI · Desktop</span>
                <h3>Hands on the machine</h3>
                <p>Real terminal, file checkpoints, browser automation, computer use.</p>
              </article>
              <article className="tile">
                <span className="tag">Gateway</span>
                <h3>Rooms you already use</h3>
                <p>One process for Telegram, Discord, Slack, and more. Same conversation everywhere.</p>
              </article>
              <article className="tile">
                <span className="tag">Mind</span>
                <h3>Memory that stays</h3>
                <p>Curated memory, self-writing skills, session search, cron that keeps firing.</p>
              </article>
            </div>
          </div>
        </section>

        <section className="section" id="join">
          <div className="wrap">
            <p className="section-kicker">04 · Waitlist</p>
            <div className="waitlist-box">
              <div>
                <h2>Get Jimmy when the loop opens.</h2>
                <p className="note">
                  Leave your details. We’ll only mail when there’s a build worth trying — laptop first,
                  then the rest of the ecosystem.
                </p>
              </div>
              <WaitlistForm />
            </div>
          </div>
        </section>
      </main>

      <footer className="site-foot">
        <span>Jimmy · personal agentic OS</span>
        <span>laptop ↔ phone ↔ cloud ↔ watch</span>
      </footer>
    </div>
  );
}
