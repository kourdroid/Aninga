## 2026-06-01 - Added visual focus states for CustomTkinter interactive widgets
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` lack native visual focus states for keyboard navigation, impairing accessibility.
**Action:** Manually bind `<FocusIn>` and `<FocusOut>` events to temporarily alter their `fg_color` or `text_color` to match their hover states, dynamically capturing the original state using `cget()`.
