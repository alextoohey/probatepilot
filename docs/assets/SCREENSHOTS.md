# Screenshots

Captured against the seeded demo estate via a headless Chromium pass through the real
running app — not mocked, not hand-picked from ideal state. Currently referenced from the
root `README.md`:

- `dashboard.png` — the hero shot: a fresh demo estate with its three CRITICAL alerts.
- `documents.png` — the upload screen with the parsing checklist.
- `chat.png` — a real, grounded RAG answer with a markdown table.
- `phoenix-trace.png` — a real Phoenix trace of a DeadlineAgent `messages.create` call:
  the exact system prompt sent, the estate JSON input, and per-call cost/token/latency.
  Captured from a local self-hosted Phoenix instance (`docker run ... arizephoenix/phoenix`,
  see `agent/README.md#phoenix-tracing`), not Phoenix Cloud — don't point this at a shared
  or teammate's Phoenix project when retaking it, since it captures real prompt/completion
  content (`PHOENIX_CAPTURE_LLM_CONTENT=true` locally).

`welcome.jpg` (the marketing landing page) is captured but not currently embedded in the
README — the dashboard does more work as the lead image. Swap it in if you'd rather open
with the landing page.

## Retaking these

```bash
make dev        # agent on :8000, web on :3000
```

Then drive a headless browser through: `/welcome` → click "Try the demo" → screenshot `/`
(dashboard) → click "Documents" → screenshot → click "Estate chat", send a message, wait for
the stream to finish → screenshot. Playwright works well for this; there's no committed
script since it's a one-off tool, not part of the app.

Note the dashboard's alert wording depends on whether the background Claude-enhanced pass
has finished by the time you screenshot (see `AppShell.tsx`'s `refreshDeadlineAgentInBackground`)
— for a polished hero shot, trigger `POST /deadline-agent` for the visitor's estate ID and
wait for it to complete (~30-45s) before capturing, rather than relying on the instant
deterministic-only alerts a fresh login shows.

A 15–30s screen-recording GIF of the full flow (upload → alert fires → chat about it)
would convert better than any single screenshot, if you want to go further.
