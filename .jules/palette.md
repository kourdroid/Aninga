## 2024-07-08 - Keyboard Focus States in CustomTkinter
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Additionally, modifying a radio button's `fg_color` only changes the inner checked circle, so `text_color` must be used to indicate focus on radio buttons.
**Action:** Manually bind `<FocusIn>` and `<FocusOut>` events to buttons and radio buttons, toggling `fg_color` for buttons and `text_color` for radio buttons to provide clear visual feedback during keyboard navigation.
