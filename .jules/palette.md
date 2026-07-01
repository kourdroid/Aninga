
## 2024-07-01 - Added Visual Keyboard Focus Indicators to Buttons and RadioButtons
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Improving accessibility requires manually binding `<FocusIn>` and `<FocusOut>` events. For radio buttons, modifying `text_color` is more effective than `fg_color` as `fg_color` only changes the inner circle.
**Action:** Always manually bind focus events for interactive CustomTkinter widgets to ensure clear visual feedback for keyboard users.
