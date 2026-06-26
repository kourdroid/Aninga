## 2026-06-26 - Keyboard Accessibility for CustomTkinter Buttons
**Learning:** CustomTkinter CTkButton and CTkRadioButton widgets do not natively provide visual focus states during keyboard navigation.
**Action:** Always manually bind <FocusIn> and <FocusOut> events to alter widget properties (fg_color for buttons, text_color for radio buttons) to ensure screen reader and keyboard-only users have visual feedback.
