## 2024-06-18 - Add visual focus states for keyboard navigation
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` lack native visual focus states for keyboard navigation. For buttons, `fg_color` should be modified, but for radio buttons, modifying `fg_color` only changes the inner checked circle, so `text_color` must be used instead to highlight focus.
**Action:** Always manually bind `<FocusIn>` and `<FocusOut>` to these widgets, using `fg_color` for buttons and `text_color` for radio buttons to ensure keyboard accessibility.
