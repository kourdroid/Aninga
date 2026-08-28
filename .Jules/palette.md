## 2026-05-24 - Missing Native Keyboard Focus States in CustomTkinter
**Learning:** CustomTkinter widgets like `CTkButton` and `CTkRadioButton` lack native visual focus states for keyboard navigation.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their visual states, dynamically capturing the original state with `widget.cget()` before modifying it.
