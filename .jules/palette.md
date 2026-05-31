
## 2024-05-31 - Add visual focus states for buttons and radio buttons
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation, reducing accessibility.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their `fg_color` or `text_color` to match hover states.
