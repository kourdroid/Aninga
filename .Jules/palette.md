## 2024-05-13 - Focus State Improvements for Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their `fg_color` or `text_color` to match hover states. Use `widget.cget("property_name")` to capture original state dynamically.
