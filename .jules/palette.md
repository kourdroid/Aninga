
## 2024-06-23 - CustomTkinter Widget Focus States
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, not the label text.
**Action:** Manually bind `<FocusIn>` and `<FocusOut>` events. Temporarily alter `fg_color` for buttons, and `text_color` for radio buttons to visually indicate keyboard focus.
