
## 2026-06-15 - Missing Native Focus States in CustomTkinter
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states for keyboard navigation, making the UI inaccessible for keyboard users.
**Action:** Manually bind `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual state. Use `fg_color` for buttons, but for radio buttons use `text_color`, as modifying a radio button's `fg_color` only changes the inner checked circle. Dynamically capture the original color with `.cget()` to restore it.
