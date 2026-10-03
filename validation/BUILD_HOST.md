# Build the Windows reference host

Requires Git, Rust 1.89.0 / Cargo 1.89.0 and the MSVC Windows C++ build toolchain. All four repositories must be siblings in a new, dedicated directory. Never replace an existing working checkout to follow this recipe.

Clone https://github.com/OctoSense-org/OctoSense-App-Hub.git as OctoSense-App-Hub and check out 0f332112f0b5a379c5bb33790df74b21597190cf.

Clone https://github.com/OctoSense-org/makepad.git as makepad and check out 1f3b1dedfbb81424eb8dbf69e5e2c634fa73dc54.

Clone https://github.com/OctoSense-org/Octoscript.git as octoscript and check out 573d694640c3d75dfa1acf09c9688b4ee4ccb508.

Clone https://github.com/OctoSense-org/Octoscript-Makepad.git as octoscript-makepad and check out cb66de073469063abeb2a5ab2a2bbf3cdb365745.

The upstream Hub lock omits serde from octoscript-ui-l0 even though the pinned source declares it. Copy this application's validation/host-Cargo.lock to the new isolated Hub checkout's Cargo.lock to use the recorded resolution. It adds precisely that dependency. The compiler, lock and executable hashes are recorded in host-build.json. Do not replace a lock in an unrelated existing workspace.

```powershell
cargo metadata --manifest-path .\OctoSense-App-Hub\Cargo.toml --format-version 1
cargo build --manifest-path .\OctoSense-App-Hub\Cargo.toml --release --locked -p octosense-card-host -p octosense-app-hub
```

Outputs: OctoSense-App-Hub/target/release/card-host.exe and hub.exe. Set OCTO_CARD_HOST to the newly built executable and run the competition application's octocard.bat. Check its bundle with that same build's hub.exe and --allow-unsigned.

Source pinning and successful compilation do not prove official acceptance or byte-identical builds across different toolchains. Consult the accompanying build status and native validation evidence for observed results.
