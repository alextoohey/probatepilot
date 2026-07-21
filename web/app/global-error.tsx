"use client";

import * as Sentry from "@sentry/nextjs";
import { useEffect } from "react";

export default function GlobalError({
  error,
}: {
  error: Error & { digest?: string };
}) {
  useEffect(() => {
    Sentry.captureException(error);
  }, [error]);

  return (
    <html>
      <body>
        <main style={{ maxWidth: 768, margin: "0 auto", padding: 24, fontFamily: "system-ui, sans-serif" }}>
          <h1 style={{ fontSize: 24, fontWeight: 600, margin: 0 }}>Something went wrong</h1>
          <p style={{ marginTop: 8, color: "#475569" }}>
            The error has been logged. Please refresh and try again.
          </p>
        </main>
      </body>
    </html>
  );
}
