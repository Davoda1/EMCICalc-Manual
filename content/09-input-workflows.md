**Definitions** stores evaluated values, unknowns and pure parameterized functions. Use clear names and check a definition before replacing one used elsewhere. Restoring saved definitions and drafts does not automatically run every saved expression.

**Input modes** keeps separate Expression, Classic and RPN state. Expression uses ordinary precedence. Classic applies operations left to right, with equals committing the result. RPN uses a stack: enter `2`, choose Enter; enter `3`, choose Enter; then choose + to combine the top two values into 5. Drop removes the top value, Swap exchanges the top two, and Roll changes stack order. Use **Insert result into Calculate** when you want to transfer the result to the main editor.

**Programmer** provides fixed-width integer calculations. Set word size, Signed/Unsigned interpretation and Checked/Wrap overflow before calculating. Enter decimal or explicit `0x`, `0b`, `0o` literals. A shift or rotation count must be smaller than the selected word width. This is separate from general fractional BIN/OCT/HEX calculation.

**Keypad designer** assigns semantic calculator actions to a custom layout. Keep essential editing and evaluation actions reachable, and save useful layouts through workspace exchange.

---

[Previous: Use the mathematical workbenches](08-workbenches.md) · [Manual contents](./) · [Next: Appearance, language and help](10-appearance-help.md)
