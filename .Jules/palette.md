## 2024-03-20 - CustomTkinter Radio Button Empty State
**Learning:** CustomTkinter `CTkRadioButton` components bound to a `StringVar` will render in an empty (unselected) visual state if the variable isn't explicitly initialized with a value that matches one of the radio buttons, potentially confusing users about what the default selection is.
**Action:** Always initialize CustomTkinter StringVars or IntVars with a `value='...'` argument that matches one of the radio button options to ensure a valid default state is visibly selected on mount.

## 2024-05-19 - Visual Feedback for Blocking Operations in CustomTkinter
**Learning:** In Tkinter/CustomTkinter, synchronous blocking operations within callbacks freeze the main UI thread. Because of this, assigning UI state changes (such as disabling a button and changing text to "Downloading...") won't visually render unless `window.update()` is called immediately after before the blocking task begins.
**Action:** Apply UI state changes and call `window.update()` prior to blocking operations, and ensure the state is reliably restored inside a `finally` block to prevent the app from getting permanently stuck in a loading state if an error occurs.

## 2026-04-30 - Focus Visibility in CustomTkinter Entries
**Learning:** In CustomTkinter, `CTkEntry` widgets with `border_width=0` lack any visual indication when they receive keyboard focus, violating basic accessibility (WCAG) guidelines for keyboard navigation.
**Action:** Always provide a visual focus state. For borderless designs, initialize the entry with a default border matching the background color (e.g., `border_width=2, border_color=bgColor`), and bind `<FocusIn>` and `<FocusOut>` to toggle the border color to a primary accent color.
