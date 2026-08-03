## 2024-07-09 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, making it ineffective for focus feedback.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`. Ensure loop variables in lambdas are captured as default arguments to prevent late-binding closure bugs.
## 2024-08-03 - CustomTkinter Keyboard Activation Missing
**Learning:** In this application's CustomTkinter components, `CTkButton` and `CTkRadioButton` lack native keyboard activation (Space/Return) when focused via Tab. While focus visuals exist, keyboard users cannot trigger actions, blocking accessibility.
**Action:** Manually bind `<space>` and `<Return>` to `w._command()` with defensive state checks for buttons, and to `w.invoke()` for radio buttons.
