## 2024-06-02 - Keyboard Focus States for CustomTkinter
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation, making them inaccessible to keyboard users.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their `fg_color` to match their `hover_color`, safely capturing their original state dynamically using `cget()`, and using default lambda arguments to avoid late-binding closure bugs.
