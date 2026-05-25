## 2026-05-25 - CustomTkinter Keyboard Focus Indicators
**Learning:** CustomTkinter CTkButton and CTkRadioButton lack native visual focus states for keyboard navigation, making them inaccessible.
**Action:** Manually bind <FocusIn> and <FocusOut> to toggle fg_color or text_color to the widget's hover_color dynamically using cget().
