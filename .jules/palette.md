## 2024-05-24 - Visual Focus States for CustomTkinter Widgets
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` lack native visual focus states during keyboard navigation.
**Action:** Manually bind `<FocusIn>` and `<FocusOut>` events to toggle visual properties (`fg_color` for buttons, `text_color` for radio buttons).
