
## 2024-06-22 - Add Keyboard Focus states to CustomTkinter buttons
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, so `text_color` must be used for radio button focus.
**Action:** Always manually bind `<FocusIn>` and `<FocusOut>` events to `fg_color` (buttons) and `text_color` (radio buttons) when developing accessible customtkinter applications.
