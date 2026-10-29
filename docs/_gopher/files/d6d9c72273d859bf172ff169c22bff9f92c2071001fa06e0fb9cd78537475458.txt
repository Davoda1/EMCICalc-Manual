Choose the runtime package for your operating system. A source ZIP or source tar.gz contains development files and is not the ready-to-run application.

| Platform | Package | Start the application |
| --- | --- | --- |
| Windows 10/11 x64 | `EMCICalc-1.0.0-Windows-x64.zip` | Extract the entire ZIP, then open `EMCICalc.exe` at its root. |
| GNU/Linux x86_64 | `EMCICalc-1.0.0-Linux-x86_64.tar.gz` | Extract the archive, then run the root-level `EMCICalc` executable. |
| Debian-compatible amd64 system | `emcicalc_1.0.0_amd64.deb` | Install the package, then open EMCICalc from your application menu or run `emcicalc`. |

Keep the supplied library, plugin, font and data directories beside the portable executable. Moving only the EXE or Linux executable separates it from its runtime dependencies. The Linux binary package requires glibc 2.38 or newer and a working graphical desktop; older systems need a compatible build from source.

For a local Debian package, use the package manager from the directory containing the download:

```bash
sudo apt install ./emcicalc_1.0.0_amd64.deb
```

The installed command is a real binary at `/usr/bin/emcicalc`. For the portable Linux package, start it from the extracted directory with `./EMCICalc`. If the executable permission was lost during copying, restore it with `chmod +x EMCICalc`.

To check a downloaded file, compare its SHA-256 with the entry in the supplied `SHA256SUM.txt`. On Windows, PowerShell's `Get-FileHash` with `-Algorithm SHA256` shows the digest. On Linux, run `sha256sum --ignore-missing -c SHA256SUM.txt` from the download directory. Check that the files you intend to use are reported as matching.

Portable refers to the application files. Your saved data is kept separately in your user profile; it is not stored beside the executable.

---

[Manual contents](./) · [Next: Get oriented](02-interface-tour.md)
