## 2024-05-20 - CustomTkinter Button Focus States
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. For radio buttons, modifying `fg_color` only changes the inner checked circle.
**Action:** Improve keyboard accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter `fg_color` for buttons and `text_color` for radio buttons.
