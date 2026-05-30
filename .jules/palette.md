
## 2024-05-24 - CustomTkinter Keyboard Focus Indicators
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets do not natively provide visual focus states during keyboard navigation. This impacts accessibility as users cannot track tabbed focus.
**Action:** Improve accessibility by manually binding `<FocusIn>` and `<FocusOut>` events to temporarily alter their `fg_color` or `text_color` to match existing hover states.
