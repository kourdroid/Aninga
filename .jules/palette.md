## 2024-06-07 - Add Keyboard Focus States for Buttons and Radio Buttons
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` lack native visual focus states for keyboard navigation. Modifying a radio button's `fg_color` only changes the inner checked circle, so `text_color` must be used for visual focus.
**Action:** Bind `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual states, using `widget.cget('property')` to safely capture the original states dynamically.
