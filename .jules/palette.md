## 2024-05-26 - Keyboard Focus States for CustomTkinter Widgets
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets do not have native visual focus states for keyboard navigation, reducing accessibility.
**Action:** Manually bind `<FocusIn>` and `<FocusOut>` events to temporarily alter their `fg_color` or `text_color` to match hover states to provide clear visual feedback to keyboard users.
