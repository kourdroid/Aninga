## 2024-05-24 - CustomTkinter Interactive Widget Focus
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation.
**Action:** Manually bind `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state (`fg_color` for buttons, `text_color` for radio buttons) using dynamically captured `cget()` properties.
