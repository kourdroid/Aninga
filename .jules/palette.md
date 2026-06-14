
## 2024-06-14 - Keyboard Focus States for CustomTkinter
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` lack native visual focus states. For buttons, `fg_color` can be modified. However, modifying a radio button's `fg_color` only changes the inner checked circle, so `text_color` must be used instead. Original states must be dynamically captured using `.cget()` in default lambda arguments to reliably restore colors on `<FocusOut>`.
**Action:** Implemented `<FocusIn>` and `<FocusOut>` events for buttons (using `fg_color`) and radio buttons (using `text_color`), dynamically capturing their original values using `.cget()` in default arguments to ensure accurate restoration.
