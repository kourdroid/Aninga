## 2024-03-20 - CustomTkinter Radio Button Empty State
**Learning:** CustomTkinter `CTkRadioButton` components bound to a `StringVar` will render in an empty (unselected) visual state if the variable isn't explicitly initialized with a value that matches one of the radio buttons, potentially confusing users about what the default selection is.
**Action:** Always initialize CustomTkinter StringVars or IntVars with a `value='...'` argument that matches one of the radio button options to ensure a valid default state is visibly selected on mount.

## 2024-05-19 - Visual Feedback for Blocking Operations in CustomTkinter
**Learning:** In Tkinter/CustomTkinter, synchronous blocking operations within callbacks freeze the main UI thread. Because of this, assigning UI state changes (such as disabling a button and changing text to "Downloading...") won't visually render unless `window.update()` is called immediately after before the blocking task begins.
**Action:** Apply UI state changes and call `window.update()` prior to blocking operations, and ensure the state is reliably restored inside a `finally` block to prevent the app from getting permanently stuck in a loading state if an error occurs.

## 2026-04-21 - Transient Inline Action Feedback
**Learning:** When UI space is severely constrained (like directly adjacent input grids), traditional persistent inline error labels below inputs aren't always feasible. However, silently returning early on validation failure leaves the user confused as to why the button click 'did nothing'.
**Action:** Utilize transient text state changes directly on the call-to-action button (e.g., changing 'Download' to 'Missing Fields!' for 2 seconds before reverting) to provide immediate, localized, and contextually relevant validation feedback without requiring structural UI shifts.
