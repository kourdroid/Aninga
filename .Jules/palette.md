## 2024-05-20 - Add focus visible styles for CustomTkinter interactive elements
**Learning:** CustomTkinter Buttons and RadioButtons lack native visual focus states when navigated via keyboard. To improve accessibility for keyboard users, `<FocusIn>` and `<FocusOut>` events can be bound to temporarily alter colors (like `fg_color` or `text_color`) to simulate a focus state.
**Action:** Manually bind focus events for interactive elements (Buttons and RadioButtons) to provide visual feedback, mirroring hover states.
