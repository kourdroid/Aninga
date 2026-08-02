## 2024-07-09 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, making it ineffective for focus feedback.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`. Ensure loop variables in lambdas are captured as default arguments to prevent late-binding closure bugs.
## 2024-05-25 - CustomTkinter Keyboard Activation
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` do not natively trigger their commands when a user presses `<space>` or `<Return>` while focused. This breaks keyboard accessibility.
**Action:** Manually bind `<space>` and `<Return>` to `_command()` for buttons (checking state first) and `invoke()` for radio buttons.
