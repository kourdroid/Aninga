
## 2024-06-03 - CustomTkinter Keyboard Focus Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events. Use `fg_color` for buttons, but for radio buttons use `text_color`, as modifying a radio button's `fg_color` only changes the inner checked circle.
