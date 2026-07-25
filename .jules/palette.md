## 2024-07-09 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, making it ineffective for focus feedback.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`. Ensure loop variables in lambdas are captured as default arguments to prevent late-binding closure bugs.
## 2024-07-25 - CustomTkinter Keyboard Interaction
**Learning:** CustomTkinter's `CTkButton` and `CTkRadioButton` components do not natively execute their commands when a keyboard user presses `<space>` or `<Return>`, making them inaccessible to keyboard users even when focused.
**Action:** Always manually bind `<space>` and `<Return>` keys to invoke the widget's action (`_command()` for buttons, `invoke()` for radio buttons). Defensively check that `w.cget('state') != 'disabled'` and `getattr(w, '_command', None)` exists to prevent bypassing application logic.
