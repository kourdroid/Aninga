## 2024-06-24 - Visual focus states for CustomTkinter interactive widgets
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. For radio buttons, modifying `fg_color` only changes the inner checked circle, so `text_color` must be used for focus indication.
**Action:** Always manually bind `<FocusIn>` and `<FocusOut>` events to interactive CustomTkinter widgets (buttons and radio buttons) to ensure keyboard accessibility.
