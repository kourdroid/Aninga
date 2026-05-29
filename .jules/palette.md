## 2024-05-30 - Add Focus States to CTkButton and CTkRadioButton
**Learning:** CustomTkinter CTkButton and CTkRadioButton widgets lack native visual focus states for keyboard navigation.
**Action:** Improve accessibility by manually binding <FocusIn> and <FocusOut> events to temporarily alter their fg_color to match hover states.
