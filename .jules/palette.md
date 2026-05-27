## 2024-05-28 - CustomTkinter Visual Focus States
**Learning:** CustomTkinter CTkButton and CTkRadioButton widgets lack native visual focus states for keyboard navigation.
**Action:** Bound <FocusIn> and <FocusOut> events to temporarily alter their fg_color or text_color to match hover states, using widget.cget() to dynamically safely capture original colors.
