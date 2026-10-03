# Host reproducibility check — 2026-10-03

Inventory: host-inventory.json. The three dependency checkouts are clean and their fixed commits match the host's declared dependencies. The tested executable retains the previously recorded SHA-256.

Existing octosense-ws dependency junctions point into an absent Documents workspace. They have been preserved; they are not a working build route. New isolated checkouts were prepared under runtime/host-repro inside the project directory, with App Hub and its three sibling dependencies at the recorded commits.

Observed commands and outcomes:

1. `cargo metadata --manifest-path runtime/host-repro/OctoSense-App-Hub/Cargo.toml --offline --locked --format-version 1`: fails because the upstream lock needs updating.
2. The same metadata command with `--offline` but without `--locked`: resolves precisely one Cargo.lock dependency addition, serde for octoscript-ui-l0. This independently reproduces the original workspace's existing lock difference, without editing that workspace.
3. Metadata then stops because convert_case 0.6.0 is absent from the local cache. Offline mode correctly prevents a network request.

This establishes a concrete build preparation path, not a successful build. Next: obtain missing dependencies in the isolated workspace, build with its resolved lock, record compiler/lock/binary hashes, then rerun native interaction and file verification against that newly built executable. No binary provenance equality or official host acceptance is claimed.

## Subsequent completed build

The isolated release build completed successfully using `cargo build --manifest-path runtime/host-repro/OctoSense-App-Hub/Cargo.toml --release --locked -p octosense-card-host -p octosense-app-hub` (exit 0, 2m24s). Fixed source revisions are in host-inventory.json; the resolved build lock is retained as host-Cargo.lock. Compiler and new binary hashes are in host-build.json.

The newly built hub.exe admitted the current bundle with --allow-unsigned. The new card-host.exe passed all twelve native UI and file-result cases independently: new-host-results.json. Test hosts were closed by their own remote quit endpoint. This supersedes the earlier build-preparation-only status; official competition acceptance remains unverified. The old binary has been preserved.
