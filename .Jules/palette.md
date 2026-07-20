## 2026-07-20 - CustomTkinter Keyboard Activation
**Learning:** CustomTkinter CTkButton and CTkRadioButton widgets do not natively execute their commands when a keyboard user presses <space> or <Return>.
**Action:** Manually bind <space> and <Return> to invoke the widget's action (e.g., via _command() for buttons or invoke() for radio buttons), checking state to prevent bypassing logic.
