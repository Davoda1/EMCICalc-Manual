The full selectable saved-data path shown by the application is authoritative. Defaults are:

- Windows: `%AppData%/davoda1/EMCICalc`
- GNU/Linux: `~/.config/davoda1/EMCICalc`

Close EMCICalc before copying the profile directory or replacing application files. Copy important unsaved text separately. A complete closed-application profile backup is the simplest recovery point.

Use **Saved workspace → Export workspace** to create an `.emci` exchange file. Select the sections you need, such as history, registers, definitions, matrices, datasets, graph configuration or custom layouts. Export excludes machine-specific paths and window geometry. Keep the exported file separately from the live profile.

Use **Import workspace**, inspect the preview and choose how to handle conflicts before applying the selected content. Imported/restored drafts are not automatically recalculated. An exchange file is convenient for selected mathematical work; it is not an exact copy of every preference in the profile directory.

Settings, history and registers use guarded atomic saves. If another instance changes the same profile, a visible conflict can preserve this instance's draft separately rather than overwrite the other instance. Close the other instance and retry. Do not remove a live lock or pending recovery journal to force a save.

---

[Previous: Appearance, language and help](10-appearance-help.md) · [Manual contents](./) · [Next: Keyboard quick reference](12-keyboard-reference.md)
