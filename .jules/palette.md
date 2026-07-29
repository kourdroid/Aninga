## 2024-07-09 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, making it ineffective for focus feedback.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`. Ensure loop variables in lambdas are captured as default arguments to prevent late-binding closure bugs.

## 2024-07-29 - Keyboard Activation for CTkButton and CTkRadioButton
**Learning:** CustomTkinter widgets like `CTkButton` and `CTkRadioButton` do not natively trigger their commands when a user presses `<space>` or `<Return>`, even if they are focusable.
**Action:** Manually bind `<space>` and `<Return>` keys to these widgets to trigger `w._command()` for buttons (after checking state and existence) and `w.invoke()` for radio buttons, ensuring full keyboard interaction support.
