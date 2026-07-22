## 2026-07-22 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter's CTkButton and CTkRadioButton widgets do not natively execute commands when a keyboard user presses Space or Return, rendering them inaccessible to keyboard-only users.
**Action:** Manually bind `<space>` and `<Return>` keys to invoke button commands (using `getattr(w, '_command')()`) and radio button selections (using `w.invoke()`), ensuring safe execution by checking if the widget is not disabled.
