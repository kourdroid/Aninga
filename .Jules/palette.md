## 2024-03-20 - CustomTkinter Radio Button Empty State
**Learning:** CustomTkinter `CTkRadioButton` components bound to a `StringVar` will render in an empty (unselected) visual state if the variable isn't explicitly initialized with a value that matches one of the radio buttons, potentially confusing users about what the default selection is.
**Action:** Always initialize CustomTkinter StringVars or IntVars with a `value='...'` argument that matches one of the radio button options to ensure a valid default state is visibly selected on mount.

## 2024-05-19 - Visual Feedback for Blocking Operations in CustomTkinter
**Learning:** In Tkinter/CustomTkinter, synchronous blocking operations within callbacks freeze the main UI thread. Because of this, assigning UI state changes (such as disabling a button and changing text to "Downloading...") won't visually render unless `window.update()` is called immediately after before the blocking task begins.
**Action:** Apply UI state changes and call `window.update()` prior to blocking operations, and ensure the state is reliably restored inside a `finally` block to prevent the app from getting permanently stuck in a loading state if an error occurs.

## 2024-05-20 - CustomTkinter Input Focus State Accessibility
**Learning:** CustomTkinter `CTkEntry` widgets with `border_width=0` lack visual focus indicators, making keyboard navigation difficult for accessibility. Users don't know which field they are typing in when tabbing.
**Action:** Always provide a default `border_width=2` that matches the background color (`border_color=inputBgColor`) and explicitly bind `<FocusIn>` and `<FocusOut>` events to toggle the `border_color` to the primary theme color, ensuring clear visual focus state while maintaining the original design intention. Use default lambda arguments (e.g., `lambda e, w=entry: w.configure(...)`) inside loops to correctly bind the widget reference.
