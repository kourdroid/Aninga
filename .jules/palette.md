## 2024-07-09 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, making it ineffective for focus feedback.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`. Ensure loop variables in lambdas are captured as default arguments to prevent late-binding closure bugs.
## 2024-07-09 - Keyboard Activation for CustomTkinter Buttons
**Learning:** CustomTkinter CTkButton and CTkRadioButton components can receive focus and have visual focus states managed via `<FocusIn>`, but they do not inherently bind `<space>` or `<Return>` to trigger their commands natively like standard Tkinter buttons do.
**Action:** Always manually bind `<space>` and `<Return>` to `widget._command()` (for buttons) and `widget.invoke()` (for radio buttons) in CustomTkinter apps to ensure full keyboard accessibility.
