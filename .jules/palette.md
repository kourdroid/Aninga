## 2026-07-13 - Keyboard Accessibility for CustomTkinter Buttons
**Learning:** CustomTkinter's `CTkButton` and `CTkRadioButton` components do not natively execute their commands when a keyboard user presses `<space>` or `<Return>`, which breaks expected keyboard navigation.
**Action:** Manually bind `<space>` and `<Return>` to `_command()` for buttons (defensively checking `state != 'disabled'` and `getattr(w, '_command', None)`) and `<space>` to `invoke()` for radio buttons.
