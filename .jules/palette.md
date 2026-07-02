
## 2024-07-02 - CustomTkinter Keyboard Focus Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` lack native visual focus states for keyboard navigation, making the app inaccessible to keyboard-only users.
**Action:** Manually bind `<FocusIn>` and `<FocusOut>` events to alter `fg_color` for buttons and `text_color` for radio buttons to provide clear visual focus indicators.
