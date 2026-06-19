## 2024-06-19 - CustomTkinter Keyboard Focus Indicators
**Learning:** CustomTkinter CTkButton and CTkRadioButton widgets lack native visual focus states for keyboard navigation. Modifying a radio button's fg_color only changes the inner checked circle.
**Action:** Manually bind <FocusIn> and <FocusOut> events to temporarily alter their visual state. Use fg_color for buttons and text_color for radio buttons.
