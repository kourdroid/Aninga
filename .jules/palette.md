## 2024-07-09 - CustomTkinter Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, making it ineffective for focus feedback.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`. Ensure loop variables in lambdas are captured as default arguments to prevent late-binding closure bugs.

## 2024-07-10 - Keyboard Activation for CTk Widgets
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` components do not natively trigger their associated actions when a keyboard user presses `<space>` or `<Return>`. This renders the UI inaccessible for pure keyboard users, even if focus states are visually indicated.
**Action:** Always manually bind `<space>` and `<Return>` to these widgets. For buttons, trigger `getattr(w, '_command')()` defensively checking if the command exists and the state is not 'disabled'. For radio buttons, use `w.invoke()`.
