## 2024-05-25 - CustomTkinter Button Keyboard Focus States
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation, making them inaccessible to keyboard users out-of-the-box.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their `fg_color` or `text_color` to match hover states.
