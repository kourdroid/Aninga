## 2026-07-21 - Keyboard Action Bindings for CustomTkinter Buttons
**Learning:** CustomTkinter's `CTkButton` and `CTkRadioButton` components do not natively execute their commands when a keyboard user presses `<space>` or `<Return>`, making them inaccessible to keyboard-only users even when they can receive focus.
**Action:** Always manually bind these keys to invoke the widget's action (e.g., via `_command()` for buttons or `invoke()` for radio buttons) and ensure the button is not disabled before execution.
