## 2026-06-29 - Keyboard Focus Accessibility for CustomTkinter Widgets
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation.
**Action:** Manually bind `<FocusIn>` and `<FocusOut>` events. Use `fg_color` for buttons, and `text_color` for radio buttons (since modifying a radio button's `fg_color` only changes the inner checked circle).
