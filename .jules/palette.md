## 2024-06-13 - Add Keyboard Focus States to Buttons and Radio Buttons
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`, as modifying a radio button's `fg_color` only changes the inner checked circle.
