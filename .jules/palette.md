## 2026-06-08 - CustomTkinter Keyboard Focus Accessibility
**Learning:** CustomTkinter CTkButton and CTkRadioButton widgets lack native visual focus states for keyboard navigation. For CTkRadioButton, modifying fg_color only changes the inner checked circle, so text_color must be modified for visual focus feedback.
**Action:** Manually bind <FocusIn> and <FocusOut> events to temporarily alter fg_color for buttons and text_color for radio buttons to improve keyboard accessibility, dynamically capturing the original state using cget().
