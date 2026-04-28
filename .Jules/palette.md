## 2024-03-20 - CustomTkinter Radio Button Empty State
**Learning:** CustomTkinter `CTkRadioButton` components bound to a `StringVar` will render in an empty (unselected) visual state if the variable isn't explicitly initialized with a value that matches one of the radio buttons, potentially confusing users about what the default selection is.
**Action:** Always initialize CustomTkinter StringVars or IntVars with a `value='...'` argument that matches one of the radio button options to ensure a valid default state is visibly selected on mount.

## 2024-05-19 - Visual Feedback for Blocking Operations in CustomTkinter
**Learning:** In Tkinter/CustomTkinter, synchronous blocking operations within callbacks freeze the main UI thread. Because of this, assigning UI state changes (such as disabling a button and changing text to "Downloading...") won't visually render unless `window.update()` is called immediately after before the blocking task begins.
**Action:** Apply UI state changes and call `window.update()` prior to blocking operations, and ensure the state is reliably restored inside a `finally` block to prevent the app from getting permanently stuck in a loading state if an error occurs.

## 2024-05-19 - Visual Focus for CTkEntry Inputs
**Learning:** CustomTkinter `CTkEntry` widgets with `border_width=0` provide no visual feedback when focused, severely degrading keyboard navigation and accessibility.
**Action:** When setting `border_width=0` for style, always assign a small default border width matching the input's background color, and use `<FocusIn>` and `<FocusOut>` event bindings to toggle the `border_color` to a primary highlight color.
