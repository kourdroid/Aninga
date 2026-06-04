
## 2024-06-04 - CustomTkinter Button Keyboard Accessibility
**Learning:** CustomTkinter `CTkButton` and `CTkRadioButton` widgets lack native visual focus states when navigated via keyboard, making them inaccessible for keyboard-only users.
**Action:** Always manually bind `<FocusIn>` and `<FocusOut>` events to interactable elements. For buttons, dynamically adjust `fg_color` to match `hover_color`. For radio buttons, adjust `text_color` instead, as changing `fg_color` only modifies the inner circle.
