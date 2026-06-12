## 2024-06-12 - CustomTkinter Keyboard Navigation Focus
**Learning:** CustomTkinter CTkButton and CTkRadioButton widgets lack native visual focus states for keyboard navigation. Modifying a radio button's fg_color only changes the inner checked circle.
**Action:** Always manually bind <FocusIn> and <FocusOut> events. Use fg_color for buttons, but for radio buttons use text_color to indicate focus.
