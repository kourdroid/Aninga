## 2024-07-09 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, making it ineffective for focus feedback.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`. Ensure loop variables in lambdas are captured as default arguments to prevent late-binding closure bugs.

## 2024-08-04 - CustomTkinter Keyboard Activation
**Learning:** CustomTkinter CTkButton and CTkRadioButton components do not natively execute their commands when a keyboard user presses Space or Return.
**Action:** Manually bind Space and Return keys to invoke the widget's action (via _command() for buttons and invoke() for radio buttons), checking if buttons are disabled before execution.
