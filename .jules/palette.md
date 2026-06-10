## 2024-05-24 - CustomTkinter Button & Radio Focus States
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` lack native keyboard focus visual states. Modifying `fg_color` works for buttons, but for radio buttons, modifying `text_color` is needed since `fg_color` only changes the inner checked circle.
**Action:** Always manually bind `<FocusIn>` and `<FocusOut>` to interactive CustomTkinter widgets to temporarily alter their visual styling (e.g., `fg_color` for buttons, `text_color` for radio buttons) during keyboard navigation.
