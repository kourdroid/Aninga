## 2024-03-20 - CustomTkinter Radio Button Empty State
**Learning:** CustomTkinter `CTkRadioButton` components bound to a `StringVar` will render in an empty (unselected) visual state if the variable isn't explicitly initialized with a value that matches one of the radio buttons, potentially confusing users about what the default selection is.
**Action:** Always initialize CustomTkinter StringVars or IntVars with a `value='...'` argument that matches one of the radio button options to ensure a valid default state is visibly selected on mount.

## 2024-05-19 - Visual Feedback for Blocking Operations in CustomTkinter
**Learning:** In Tkinter/CustomTkinter, synchronous blocking operations within callbacks freeze the main UI thread. Because of this, assigning UI state changes (such as disabling a button and changing text to "Downloading...") won't visually render unless `window.update()` is called immediately after before the blocking task begins.
**Action:** Apply UI state changes and call `window.update()` prior to blocking operations, and ensure the state is reliably restored inside a `finally` block to prevent the app from getting permanently stuck in a loading state if an error occurs.
## 2026-05-06 - CustomTkinter CTkEntry Focus States
**Learning:** CustomTkinter `CTkEntry` widgets configured with `border_width=0` completely lack visual focus indicators, making the application difficult to navigate via keyboard or identify the currently active input field.
**Action:** Always provide visual focus states for input fields. For `CTkEntry`, initialize a constant border width (e.g., `border_width=2`) matching the background color to prevent layout shift, and bind `<FocusIn>` and `<FocusOut>` events to toggle the `border_color` to a primary color, taking care to use default arguments in loop-generated lambdas to avoid late-binding closure bugs.
