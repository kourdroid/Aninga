## 2024-06-27 - CustomTkinter Interactive Widget Focus States
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation, making them inaccessible to keyboard-only users by default.
**Action:** Always manually bind `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state (e.g., `fg_color` for buttons, `text_color` for radio buttons) to ensure focus visibility.
