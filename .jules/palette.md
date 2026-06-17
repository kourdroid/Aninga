
## 2026-06-17 - CustomTkinter Keyboard Focus Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation, making them inaccessible for keyboard-only users.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events. For buttons, temporarily alter `fg_color`. For radio buttons, alter `text_color` since modifying a radio button's `fg_color` only changes the inner checked circle.
