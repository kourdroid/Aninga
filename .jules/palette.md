## 2024-07-09 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, making it ineffective for focus feedback.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`. Ensure loop variables in lambdas are captured as default arguments to prevent late-binding closure bugs.

## 2026-07-28 - Missing Keyboard Bindings on CustomTkinter Widgets
**Learning:** CustomTkinter's `CTkButton` and `CTkRadioButton` components do not natively execute their commands when a keyboard user presses `<space>` or `<Return>`, unlike native HTML buttons.
**Action:** Always manually bind `<space>` and `<Return>` keys to invoke the widget's action (e.g., via `_command()` for buttons or `invoke()` for radio buttons) while properly checking the `state` attribute to ensure accessibility.
