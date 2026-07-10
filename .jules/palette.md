## 2024-07-09 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, making it ineffective for focus feedback.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`. Ensure loop variables in lambdas are captured as default arguments to prevent late-binding closure bugs.

## 2024-07-10 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter's `CTkButton` and `CTkRadioButton` lack native keyboard bindings (e.g., `<space>` or `<Return>`) to trigger their actions when focused, impacting accessibility for keyboard-only users.
**Action:** Manually bind `<space>` and `<Return>` to `_command()` for buttons and `invoke()` for radio buttons, ensuring defensive checks for the disabled state (`w.cget('state') != 'disabled'`) are included.
