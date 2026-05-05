## 2024-03-20 - CustomTkinter Radio Button Empty State
**Learning:** CustomTkinter `CTkRadioButton` components bound to a `StringVar` will render in an empty (unselected) visual state if the variable isn't explicitly initialized with a value that matches one of the radio buttons, potentially confusing users about what the default selection is.
**Action:** Always initialize CustomTkinter StringVars or IntVars with a `value='...'` argument that matches one of the radio button options to ensure a valid default state is visibly selected on mount.

## 2024-05-19 - Visual Feedback for Blocking Operations in CustomTkinter
**Learning:** In Tkinter/CustomTkinter, synchronous blocking operations within callbacks freeze the main UI thread. Because of this, assigning UI state changes (such as disabling a button and changing text to "Downloading...") won't visually render unless `window.update()` is called immediately after before the blocking task begins.
**Action:** Apply UI state changes and call `window.update()` prior to blocking operations, and ensure the state is reliably restored inside a `finally` block to prevent the app from getting permanently stuck in a loading state if an error occurs.
## $(date +%Y-%m-%d) - Focus Visible Styles in CustomTkinter loops
**Learning:** When using loops to add visual focus indicators (`<FocusIn>` and `<FocusOut>`) to multiple CustomTkinter elements (like `CTkEntry`), binding a standard lambda (e.g., `lambda e: entry.configure(...)`) fails because Python closures capture loop variables by reference (late-binding), meaning all callbacks will only target the final element in the loop.
**Action:** Always capture loop variables by value in Tkinter bindings using default keyword arguments: `lambda e, w=entry: w.configure(...)`.
