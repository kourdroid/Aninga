## 2024-07-09 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, making it ineffective for focus feedback.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`. Ensure loop variables in lambdas are captured as default arguments to prevent late-binding closure bugs.
## 2024-08-06 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter's `CTkButton` and `CTkRadioButton` components do not natively execute their commands when a keyboard user presses `<space>` or `<Return>`.
**Action:** Manually bind these keys to invoke the widget's action (via `_command()` for buttons or `invoke()` for radio buttons), and always defensively check that the button is not disabled (`w.cget('state') != 'disabled'`) and the command exists to prevent bypassing application logic.
