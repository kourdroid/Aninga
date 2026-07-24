## 2024-07-09 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, making it ineffective for focus feedback.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`. Ensure loop variables in lambdas are captured as default arguments to prevent late-binding closure bugs.

## 2024-07-24 - Keyboard Action Accessibility
**Learning:** CustomTkinter's `CTkButton` and `CTkRadioButton` do not natively trigger commands when a keyboard user presses <space> or <Return>, breaking expected keyboard interaction.
**Action:** Manually bind `<space>` and `<Return>` to invoke actions (e.g., `_command()` for buttons or `invoke()` for radio buttons), ensuring to check button state (`w.cget('state') != 'disabled'`) before execution.
