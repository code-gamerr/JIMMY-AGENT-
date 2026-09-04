"""One-shot: mirror Azure OpenAI env into Jimmy profile .env files (container)."""
import os
from pathlib import Path

KEYS = (
    "AZURE_OPENAI_API_KEY",
    "AZURE_FOUNDRY_API_KEY",
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_FOUNDRY_BASE_URL",
    "AZURE_OPENAI_DEPLOYMENT",
    "AZURE_OPENAI_API_VERSION",
)


def upsert(path: Path, key: str, value: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines() if path.is_file() else []
    prefix = f"{key}="
    out: list[str] = []
    found = False
    for line in lines:
        if line.startswith(prefix) or line.startswith(f"export {prefix}"):
            if not found:
                out.append(f"{key}={value}")
                found = True
            continue
        out.append(line)
    if not found:
        if out and out[-1].strip():
            out.append("")
        out.append(f"{key}={value}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    homes = [Path("/opt/data")] + [
        Path(f"/opt/data/profiles/jimmy{i}") for i in range(1, 5)
    ]
    for home in homes:
        env = home / ".env"
        n = 0
        for key in KEYS:
            val = os.environ.get(key, "").strip()
            if val:
                upsert(env, key, val)
                n += 1
        names = sorted(
            {
                ln.split("=", 1)[0]
                for ln in (
                    env.read_text(encoding="utf-8").splitlines()
                    if env.is_file()
                    else []
                )
                if "=" in ln and not ln.strip().startswith("#")
            }
        )
        print(f"{home}: wrote={n} keys_present={names}")
    print("OK")


if __name__ == "__main__":
    main()
