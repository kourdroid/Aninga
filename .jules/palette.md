## 2024-07-01 - Add keyboard focus states for interactive widgets
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` lack native visual focus states. Enhancing `fg_color` for buttons and `text_color` for radio buttons greatly aids keyboard navigation accessibility.
**Action:** Always manually bind `<FocusIn>` and `<FocusOut>` events for interactive widgets in CustomTkinter if keyboard navigation is required.
