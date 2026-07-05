## 2024-11-20 - Keyboard Focus States for CustomTkinter
**Learning:** CustomTkinter CTkButton and CTkRadioButton lack native visual focus states when navigated via keyboard. Modifying radio button fg_color only changes the inner circle; text_color must be used for focus feedback.
**Action:** Manually bind <FocusIn> and <FocusOut> events to temporarily alter fg_color for buttons and text_color for radio buttons.
