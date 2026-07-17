## 2024-05-27 - Keyboard activation for CustomTkinter widgets
**Learning:** CustomTkinter buttons and radio buttons natively support visual focus but do not execute their commands when a keyboard user presses `<space>` or `<Return>`.
**Action:** We must manually bind these keys to trigger `_command()` (for buttons) or `invoke()` (for radio buttons), while also ensuring the button is not disabled via `widget.cget('state') != 'disabled'`.
