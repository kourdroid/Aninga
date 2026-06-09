## 2024-06-09 - Add visual focus states to buttons and radio buttons
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, so `text_color` should be used instead.
**Action:** Manually bound `<FocusIn>` and `<FocusOut>` events to these widgets to temporarily alter their visual state (`fg_color` for buttons, `text_color` for radio buttons), improving keyboard accessibility.
