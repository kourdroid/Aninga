## 2024-06-21 - CustomTkinter Keyboard Focus Indicators
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` lack native visual focus states for keyboard navigation, requiring manual binding of `<FocusIn>` and `<FocusOut>` to `fg_color` or `text_color`.
**Action:** Implemented dynamic focus binding loops with default lambda arguments (`lambda e, w=widget: w.configure(...)`) to apply pseudo-focus styles without hardcoded themes breaking.
